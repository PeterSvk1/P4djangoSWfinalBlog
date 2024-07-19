from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post
from cloudinary.models import CloudinaryField

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