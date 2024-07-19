from django.urls import path
from .views import Home, Postdetail

urlpatterns = [
    
    path('', Home.as_view(), name='home'),
    path('posts/<int:pk>', Postdetail.as_view(), name='details'),
  
]