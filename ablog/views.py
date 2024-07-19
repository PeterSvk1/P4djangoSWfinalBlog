from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post




# Create your views here.
class Home(ListView):
    model = Post 
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 4

class Postdetail(DetailView):
    model = Post
    template_name= 'details.html'