import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.db.transaction import atomic, non_atomic_requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_safe, require_http_methods

from blog.forms import PostForm, CommentForm
from blog.models import Post, Category, Comment




# Create your views here.


def main_page(request):
    categories = Category.objects.all()
    res = render(request, "blog/index.html", {"categories": categories})
    return res

def category_list(request, pk):
    category = Category.objects.get(pk=pk)
    posts = category.post_set.all()
    return render(request, "blog/category_list.html", {"category": category, "posts": posts})



def create_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "blog/create.html", {"form": form})

    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
        return redirect("view_post", pk=form.pk)

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, "blog/create.html", {"form": form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect("main")

def view_post(request, pk):
    if request.method == "GET":
        post = Post.objects.get(pk=pk)
        post.view += 1
        post.save()
        comments = post.comments.all()
        form = CommentForm()
        return render(request, "blog/view_post.html", {"post": post, "pk":pk, "comments":comments, "form":form})
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form)
            form=form.save(commit=False)
            print(form)
            form.post = Post.objects.get(pk=pk)
            form.save()
            print(form)
        return redirect("view_post", pk=pk)

def add_like(request, pk):
    post = Post.objects.get(pk=pk)
    post.like += 1
    post.save()
    return redirect("view_post", pk=pk)

def my_login(request):
    if request.method == "GET":
        return render(request, "blog/login.html")
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else: return redirect("login")

def my_logout(request):
    logout(request)


def regist(request):
    if request.method == "GET":
        return render(request, "blog/register.html")
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        try:
            us = User.objects.get(username=username)
            return redirect("main")
        except:
            user = User.objects.create_user(username=username, password=password)
            return redirect("main")

def boot(request):
    return render(request, "blog/boot.html")


def rest(request):
    a = json.dumps({"name": 141412})
    return JsonResponse(a, safe=False)

















