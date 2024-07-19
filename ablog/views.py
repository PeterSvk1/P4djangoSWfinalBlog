from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy,reverse
from .models import Post, Category
from .forms import PostForm, EditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect




# Create your views here.
class Home(ListView):
    queryset = Post.objects.all().order_by("post_date").filter(status=1) 
    template_name = 'home.html'
    paginate_by = 10

class Postdetail(DetailView,LoginRequiredMixin):
    model = Post
    template_name= 'details.html'

class NewPost(CreateView,LoginRequiredMixin):
    model = Post
    template_name = 'newpost.html'
    form_class = PostForm
   # success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            post= form.save(commit=False)
            post.author= get_object_or_404(User, id=self.request.user.id)
            post.save()
            pk= post.id 
            return HttpResponseRedirect(reverse('details', args=[str(pk)]))


class EditPost(UpdateView,LoginRequiredMixin):
    model= Post
    form_class = EditForm
    template_name = 'editpost.html'

class DeletePost(DeleteView,LoginRequiredMixin):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

class Categorys(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'
        