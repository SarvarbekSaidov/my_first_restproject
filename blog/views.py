from rest_framework import viewsets
from django.http import HttpResponse
from .models import BlogCategory, BlogAuthor, BlogPost, PostComment
from .serializers import BlogCategorySerializer, BlogAuthorSerializer, BlogPostSerializer, PostCommentSerializer
# Create your views here.

def home(request):
    return HttpResponse("Welcome to My first project in Django Rest-framework!")

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogAuthorViewSet(viewsets.ModelViewSet):
    queryset = BlogAuthor.objects.all()
    serializer_class = BlogAuthorSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer