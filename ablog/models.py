from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
default_image1= "https://res.cloudinary.com/dg5lyidc8/image/upload/v1721074029"
default_image2= "/static/images/default.4feffe0b7f2d.png"
default_image= default_image1 + default_image2

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    category = models.CharField(max_length=200, default='starwars')
    featured_image = CloudinaryField('image', default=default_image)
    status = models.IntegerField(choices=STATUS, default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

