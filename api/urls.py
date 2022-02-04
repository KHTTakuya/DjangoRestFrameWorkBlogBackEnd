from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import BlogViewSet, CreateUserView, CommentViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('blog', BlogViewSet)
router.register('comment', CommentViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('', include(router.urls)),
]
