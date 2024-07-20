from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post, Category, Comment
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User


class Home(ListView):
    model = Post 
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(author__username__icontains=query),status=1
            ).distinct().order_by('-post_date')
        return Post.objects.filter(status=1).order_by('-post_date')
        #return Post.objects.all().order_by('-post_date')

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        cat_menu = Category.objects.all()
        context['cat_menu'] = cat_menu
        context['search'] = self.request.GET.get('search', '')
        return context


class Postdetail(DetailView):
    model = Post
    template_name= 'details.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Postdetail,self).get_context_data(*args, **kwargs)
        post = self.get_object()
        
        hearts = get_object_or_404(Post, id=self.kwargs['pk'])
        totallikes= hearts.totallikes()

        liked = False
        if hearts.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        
        total_comments = post.total_comments()
        context['cat_menu'] = Category.objects.all()
        context["totallikes"]=totallikes
        context["liked"]=liked
        context["total_comments"] = total_comments 
        

        return context



class NewPost(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'newpost.html'
    
    def form_valid(self, form):
        if form.is_valid():
            post= form.save(commit=False)
            post.author= get_object_or_404(User, id=self.request.user.id)
            post.status = 0  # Set post status to 'Draft'
            post.save()
            messages.success(self.request, 'Your post has been submitted and is awaiting approval by the admin.')
            pk= post.id 
            return HttpResponseRedirect(reverse('details', args=[str(pk)]))
            





class EditPost(UpdateView):
    model= Post
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
        
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)

class Categorys(CreateView):
    model = Category
    
    template_name = 'category.html'
    fields = '__all__'

class Viewaddcomment(CreateView):

    model = Comment
    form_class= CommentForm
    template_name = 'addcomment.html'


    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
 
        form.instance.name = self.request.user.username 
        messages.success(self.request, 'Comment added!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.kwargs['pk']})


def SectionView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request,'categories.html', {'cats':cats.title(), 'category_posts':category_posts})



def ViewAllcategories(request):
    cat_all = Category.objects.all()
    return render(request,'allcategories.html', {'cat_all':cat_all})

    
    

def ViewLike(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('postid'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

