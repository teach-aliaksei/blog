from selenium import webdriver
import unittest
import os

from selenium.webdriver.common.by import By

from django.test import LiveServerTestCase



class NewTest(LiveServerTestCase):

    def test_one(self):
        print(os.environ)
        self.browser.get("http://127.0.0.1:8000/blog/")
        print(self.browser)
        self.assertIn("Title", self.browser.title)

    def test_two(self):
        self.browser.get("http://127.0.0.1:8000/blog/")
        print(self.browser)
        self.assertIn("Title", self.browser.title)

    def test_three(self):
        self.browser.get("http://127.0.0.1:8000/blog/")
        text = self.browser.find_element(By.ID, "id_p").text
        self.assertEqual("Main Page", text)


    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()





