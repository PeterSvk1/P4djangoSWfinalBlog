from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from .models import Post, Category, Comment, Profile, ContactMessage
from .forms import PostForm, EditForm, CommentForm, ContactForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import os


class Home(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        sort_by = self.request.GET.get('sort_by', 'date')
        queryset = Post.objects.filter(status=1)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            ).distinct()

        if sort_by == 'likes':
            queryset = queryset.annotate(num_likes=Count('likes')).order_by('-num_likes', '-post_date')
        else:
            queryset = queryset.annotate(num_likes=Count('likes')).order_by('-post_date')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        query = self.request.GET.get('search', '')
        context['cat_menu'] = Category.objects.all()
        context['search'] = query
        context['sort_by'] = self.request.GET.get('sort_by', 'date')
        context['total_posts'] = Post.objects.filter(status=1).count()
        context['no_results'] = not self.get_queryset().exists() and query
        return context


class Postdetail(DetailView):
    model = Post
    template_name = 'details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Postdetail, self).get_context_data(*args, **kwargs)
        post = self.get_object()

        totallikes = post.totallikes()

        liked = False
        downvoted = False
        if self.request.user.is_authenticated:
            liked = post.likes.filter(id=self.request.user.id).exists()
            upvoted_comments = post.comments.filter(upvotes=self.request.user)
            downvoted_comments = post.comments.filter(downvotes=self.request.user)
        else:
            upvoted_comments = []
            downvoted_comments = []

        total_comments = post.total_comments()
        context['cat_menu'] = Category.objects.all()
        context["totallikes"] = totallikes
        context["liked"] = liked
        context["total_comments"] = total_comments
        context['upvoted_comments'] = upvoted_comments
        context['downvoted_comments'] = downvoted_comments

        return context


class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newpost.html'

    def form_valid(self, form):
        if form.is_valid():
            post = form.save(commit=False)
            post.author = get_object_or_404(User, id=self.request.user.id)
            post.status = 1  # draft or published
            post.save()
            messages.success(self.request, 'Post is created')
            pk = post.id
            return HttpResponseRedirect(reverse('details', args=[str(pk)]))


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editpost.html'

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)


def about(request):
    return render(request, 'about.html')


class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)


class Categorys(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'


class Viewaddcomment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'addcomment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        messages.success(self.request, 'Comment added!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.kwargs['pk']})


def SectionView(request, cats):
    category = get_object_or_404(Category, name__iexact=cats.strip())
    category_posts = Post.objects.filter(category=cats, status=1).order_by('-post_date')
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts': category_posts})


def ViewAllcategories(request):
    cat_all = Category.objects.all()
    return render(request,'allcategories.html', {'cat_all':cat_all})


@login_required
def ViewLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('postid'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('details', args=[str(pk)]))


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id

    # Ensure correct permission check
    if request.user.username == comment.name or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'Sorry not allowed.')

    return redirect('details', pk=post_id)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the contact message
            ContactMessage.objects.create(email=email, message=message)

            # Send a confirmation email
            subject = 'Thank you for contacting us!'
            message = f'Hi,\n\nThank you for EMAIL.\n\nMessage\n{message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, from_email, [email], fail_silently=False)

            # Send an email notification to the site admin
            admin_subject = 'New Contact Form Submission'
            admin_message = f'New email from {email}.\n\nMessage:\n{message}'
            admin_email = os.environ.get('EMAIL_HOST_USER')
            send_mail(admin_subject, admin_message, from_email, [admin_email], fail_silently=False)

            messages.success(request, 'Message was sent!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


class ShowUserProfile(DetailView):
    model = Profile
    template_name = 'userprofiles.html'
    context_object_name = 'current_user'

    def get_context_data(self, **kwargs):
        context = super(ShowUserProfile, self).get_context_data(**kwargs)
        current_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter(author=current_user.user, status=1).order_by('-post_date')
        context["current_user"] = current_user
        context["user_posts"] = user_posts
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edituserprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)


@login_required
def upvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user

    if comment.upvotes.filter(id=user.id).exists():
        comment.upvotes.remove(user)
        messages.success(request, 'You have removed your upvote.')
    else:
        if comment.downvotes.filter(id=user.id).exists():
            comment.downvotes.remove(user)
        comment.upvotes.add(user)
        messages.success(request, 'You have upvoted the comment.')

    return redirect('details', pk=comment.post.id)


@login_required
def downvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user

    if comment.downvotes.filter(id=user.id).exists():
        comment.downvotes.remove(user)
        messages.success(request, 'You have removed your downvote.')
    else:
        if comment.upvotes.filter(id=user.id).exists():
            comment.upvotes.remove(user)
        comment.downvotes.add(user)
        messages.success(request, 'You have downvoted the comment.')

    return redirect('details', pk=comment.post.id)
