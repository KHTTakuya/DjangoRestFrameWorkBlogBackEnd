from rest_framework import viewsets
from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import BlogSerializer, UserSerializer, CommentSerializer, CategorySerializer
from rest_framework.permissions import AllowAny
from .models import Blog, Comment, Category


class FilterCategory(filters.FilterSet):
    category = filters.CharFilter(field_name="category", lookup_expr='exact')

    class Meta:
        model = Blog
        fields = ['category']


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    filter_class = FilterCategory


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
