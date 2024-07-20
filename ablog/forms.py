from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post,Category,Comment
from cloudinary.models import CloudinaryField



choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','featured_image','content','excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title please'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
            'excerpt': SummernoteWidget(attrs={'class': 'summernote', 'placeholder': 'Something short to describe your blog'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','featured_image','content','excerpt')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
            'excerpt': SummernoteWidget(attrs={'class': 'summernote', 'placeholder': 'Something short to describe your blog'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets ={
            #'name': forms.TextInput(attrs={'class':'form-control','placeholder':'use your username'}),
            #'content': SummernoteWidget(),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Please write something nice'}),
            }

