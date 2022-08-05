
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from blog.views import main_page, category_list, create_post, edit_post, view_post, add_like, my_login, regist, boot, rest


urlpatterns = [
    path('', main_page, name="main"),
    path('category/<int:pk>/', category_list, name="category"),
    path('post/create/', create_post, name="create_post"),
    path('post/edit/<int:pk>/', edit_post, name="edit_post"),
    path('post/<int:pk>/', view_post, name="view_post"),
    path('post/add_like/<int:pk>/', add_like, name="add_like"),
    path('login/', my_login, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('reg/', regist, name="regist"),
    path('boot/', boot, name="boot"),
    path('rest/', rest),
]
