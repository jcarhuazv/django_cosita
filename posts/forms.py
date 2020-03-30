from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )
        labels = {
            'title': 'Insert Title',
            'content': 'Write Content',
        }
