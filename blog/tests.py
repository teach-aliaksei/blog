from django.test import TestCase
from django.urls import resolve

from django.http import HttpRequest

from blog.models import Category
from blog.views import main_page


class MyTest(TestCase):

    def test_one(self):
        func = resolve("/blog/")
        self.assertEqual(func.func, main_page)

    def test_two(self):
        request = HttpRequest()
        response = main_page(request)
        self.assertIn("<title>Title</title>", response.content.decode())
        response = self.client.get("/blog/")
        self.assertTemplateUsed(response, "blog/index.html")

    def test4(self):
        a = Category()
        a.name = "Hello"
        a.save()

        response = self.client.post("/blog/post/create/", data={'title': 'Some title', 'text': 'Some text', 'category': '1', 'view': '4',
 'img': ''})
        self.assertEqual(response.status_code, 302)
        response = self.client.get("http://127.0.0.1:8000/blog/post/1/")
        self.assertIn("Some title", response.content.decode())

    def test5(self):
        a = Category()
        a.name = "Hello1"
        a.save()

        b = Category()
        b.name = "Hello2"
        b.save()

        self.assertEqual(2, Category.objects.all().count())

        obj = Category.objects.first()
        self.assertEqual(obj.name, "Hello1")

    def test6(self):
        a = Category()
        a.name = "Hello1"
        a.save()
        response = self.client.get("/blog/")
        self.assertIn("Hello1", response.content.decode())











