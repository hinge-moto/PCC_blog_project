from dataclasses import fields
from django import forms

from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Post Title', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100, 'rows': 30})}