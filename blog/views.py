from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import BlogCategory, BlogPost, BlogAuthor, PostComment
from .serializers import BlogCategorySerializer, BlogPostSerializer, BlogAuthorSerializer, PostCommentSerializer

class BlogCategoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            category = BlogCategory.objects.get(pk=pk)
            serializer = BlogCategorySerializer(category)
        else:
            categories = BlogCategory.objects.all()
            serializer = BlogCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = BlogCategory.objects.get(pk=pk)
        serializer = BlogCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = BlogCategory.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            post = BlogPost.objects.get(pk=pk)
            serializer = BlogPostSerializer(post)
        else:
            posts = BlogPost.objects.all()
            serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = BlogPost.objects.get(pk=pk)
        serializer = BlogPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = BlogPost.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogAuthorAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            author = BlogAuthor.objects.get(pk=pk)
            serializer = BlogAuthorSerializer(author)
        else:
            authors = BlogAuthor.objects.all()
            serializer = BlogAuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogAuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = BlogAuthor.objects.get(pk=pk)
        serializer = BlogAuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = BlogAuthor.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
