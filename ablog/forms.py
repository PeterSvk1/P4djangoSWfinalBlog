from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Category, Comment, Profile
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'category', 'content', 'excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tltle'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
            'excerpt': SummernoteWidget(attrs={'class': 'summernote', 'placeholder': 'Text'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'category', 'content', 'excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
            'excerpt': SummernoteWidget(attrs={'class': 'summernote', 'placeholder': 'text'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', }),
            }


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', }))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', }))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', }),
        }
