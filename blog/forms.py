from django.core import validators
from django.forms import ModelForm
from django import forms

from blog.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

