from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Category, Comment, Profile
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','featured_image','category','content','excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'tltle'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
            'excerpt': SummernoteWidget(attrs={'class': 'summernote', 'placeholder': 'Something short to describe your blog'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','featured_image','category','content','excerpt')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
            'excerpt': SummernoteWidget(attrs={'class': 'summernote', 'placeholder': 'Something short to describe your blog'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets ={
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Please write something nice'}),
            }

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture','bio')
        widgets = {
             'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
              'bio': forms.Textarea(attrs={'class':'form-control',}),
           

        }