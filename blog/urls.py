from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogCategoryAPIView, BlogPostAPIView, BlogAuthorAPIView, PostCommentViewSet

router = DefaultRouter()
router.register(r'comments', PostCommentViewSet)

urlpatterns = [
    path('categories/', BlogCategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', BlogCategoryAPIView.as_view(), name='category-detail'),
    path('posts/', BlogPostAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', BlogPostAPIView.as_view(), name='post-detail'),
    path('authors/', BlogAuthorAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', BlogAuthorAPIView.as_view(), name='author-detail'),
    path('', include(router.urls)),
]
