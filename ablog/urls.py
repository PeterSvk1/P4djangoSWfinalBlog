from django.urls import path
from .views import Home, Postdetail,NewPost, EditPost, DeletePost,Categorys,ViewLike

urlpatterns = [
    
    path('', Home.as_view(), name='home'),
    path('posts/<int:pk>', Postdetail.as_view(), name='details'),
    path('articles/', NewPost.as_view(), name='newpost'),
    path('articles/edit/<int:pk>', EditPost.as_view(), name='editpost'),
    path('articles/delete/<int:pk>', DeletePost.as_view(), name='deletepost'),
    path('category/', Categorys.as_view(), name='category'),
    path('like/<int:pk>', ViewLike, name='likeposts'),
  
]