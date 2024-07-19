from django.urls import path
from .views import Home, Postdetail,NewPost

urlpatterns = [
    
    path('', Home.as_view(), name='home'),
    path('posts/<int:pk>', Postdetail.as_view(), name='details'),
    path('articles/', NewPost.as_view(), name='newpost'),
  
]