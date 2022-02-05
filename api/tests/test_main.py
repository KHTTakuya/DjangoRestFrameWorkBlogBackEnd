from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Blog, User, Category
from api.serializers import BlogSerializer


class BlogModelTests(TestCase):

    def test_is_empty(self):
        saved_blogs = Blog.objects.all()
        self.assertEqual(saved_blogs.count(), 0)
