from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy,reverse
from .models import Post




# Create your views here.
class Home(ListView):
    queryset = Post.objects.all().order_by("post_date").filter(status=1) 
    template_name = 'home.html'
    paginate_by = 10

class Postdetail(DetailView):
    model = Post
    template_name= 'details.html'

class NewPost(CreateView):
    model = Post
    template_name = 'newpost.html'
    success_url = reverse_lazy('home')
