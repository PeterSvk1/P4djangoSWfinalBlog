from django.urls import path
from .views import Home, Postdetail, NewPost, EditPost, DeletePost, Categorys
from .views import SectionView, EditProfileView
from .views import Viewaddcomment, about, upvote_comment, delete_comment
from .views import contact_view, downvote_comment, ShowUserProfile, ViewLike

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('posts/<int:pk>', Postdetail.as_view(), name='details'),
    path('articles/', NewPost.as_view(), name='newpost'),
    path('category/', Categorys.as_view(), name='category'),
    path('articles/edit/<int:pk>', EditPost.as_view(), name='editpost'),
    path('articles/delete/<int:pk>', DeletePost.as_view(), name='deletepost'),
    path('categorys/<str:cats>/', SectionView, name='category'),
    path('like/<int:pk>', ViewLike, name='likeposts'),
    path('posts/<int:pk>/comment/', Viewaddcomment.as_view(), name='comments'),
    path('about', about, name='about'),
    path(
        'comment/<int:comment_id>/upvote/',
        upvote_comment, name='upvote_comment'
        ),
    path(
        'comment/<int:comment_id>/delete/',
        delete_comment, name='delete_comment'),
    path(
        'comment/<int:comment_id>/downvote/',
        downvote_comment, name='downvote_comment'),
    path('contact/', contact_view, name='contact'),
    path('<int:pk>/profile/', ShowUserProfile.as_view(), name='userprofile'),
    path(
        '<int:pk>/editprofile/', EditProfileView.as_view(),
        name='editprofile'
        ),
]
