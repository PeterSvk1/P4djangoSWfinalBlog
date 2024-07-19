from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    category = models.CharField(max_length=200, default='starwars')
    featured_image = CloudinaryField('image', default=default_image)
    status = models.IntegerField(choices=STATUS, default=0)
