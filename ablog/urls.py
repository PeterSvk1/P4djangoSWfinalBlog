from django.urls import path
from .views import Home, Postdetail,NewPost, EditPost

urlpatterns = [
    
    path('', Home.as_view(), name='home'),
    path('posts/<int:pk>', Postdetail.as_view(), name='details'),
    path('articles/', NewPost.as_view(), name='newpost'),
     path('articles/edit/<int:pk>', EditPost.as_view(), name='editpost'),
  
]