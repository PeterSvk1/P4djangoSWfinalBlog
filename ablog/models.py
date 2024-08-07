from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
default_image1 = "https://res.cloudinary.com/dg5lyidc8/image/upload/"
default_image2 = "v1721074029/static/images/default.4feffe0b7f2d.png"
default_image = default_image1 + default_image2


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    category = models.CharField(max_length=200, default='starwars')
    featured_image = CloudinaryField('image', default=default_image)
    likes = models.ManyToManyField(User, related_name='blogposts')
    status = models.IntegerField(choices=STATUS, default=0)

    def total_comments(self):
        return self.comments.count()

    def totallikes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=200, default='starwars')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(
        User, related_name='comment_upvotes', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='comment_downvotes', blank=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.post.pk})

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(default='starwarsfan')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('home')


class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.email} on {self.created_at}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
