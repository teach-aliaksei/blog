from django.contrib.auth.models import User, AbstractUser
from django.core import validators
from django.db import models

# Create your models here.
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    view = models.IntegerField(default=0)
    img = models.ImageField(upload_to="blog/", blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

