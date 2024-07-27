from django.contrib import admin
from .models import Post, Category, Comment, Profile, ContactMessage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'post_date')
    search_fields = ['title', 'content']
    list_filter = ('status',)
    summernote_fields = ('content', 'excerpt')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email', 'message')


admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Category)
