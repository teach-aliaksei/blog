from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.views import View
from django.views.decorators.http import require_GET, require_POST, require_safe, require_http_methods

from blog.forms import PostForm, CommentForm
from blog.models import Post, Category, Comment



# Create your views here.

def main_page(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 2)
    if "page" in request.GET:
        page_num = request.GET["page"]
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    messages.add_message(request, messages.SUCCESS, "Hello world")
    print(request.COOKIES)

    res = render(request, "blog/index.html", {"categories": categories, "page": page, "cats": page.object_list})
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
    request.user.pk
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
            form=form.save(commit=False)
            form.save()
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













