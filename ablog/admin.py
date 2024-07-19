from django.contrib import admin
from .models import Post,Comment
from django_summernote.admin import SummernoteModelAdmin

#
 #Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'post_date')
    search_fields = ['title', 'content']
    list_filter = ('status',)
    summernote_fields = ('content',)



admin.site.register(Comment)