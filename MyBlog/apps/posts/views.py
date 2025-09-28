from django.shortcuts import render, get_object_or_404
# from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        if not posts:
            return Response({"detail": "No posts found."}, status=404)
        else:
            pass
        # Serialize the posts using a serializer
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailAPIView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        # Serialize the post using a serializer
        serializer = PostSerializer(post)
        return Response(serializer.data)

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        # return render(request, 'posts/post_detail.html', {'post': serializer.data})
        return Response(serializer.data)
    
    def get_author_posts(self, request, author_id):
        posts = Post.objects.filter(author_id=author_id)
        serializer = PostSerializer(posts, many=True)
        # return render(request, 'posts/author_posts.html', {'posts': serializer.data})
        return Response(serializer.data)

    def get_author_name_posts(self, request, author_name):
        posts = Post.objects.filter(author__name=author_name)
        serializer = PostSerializer(posts, many=True)
        # return render(request, 'posts/author_posts.html', {'posts': serializer.data})
        return Response(serializer.data)

class PostAuthorView(APIView):
    def get(self, request, author_id=None, author_name=None):
        if author_id:
            posts = Post.objects.filter(author_id=author_id)
            serializer = PostSerializer(posts, many=True)
        elif author_name:
            posts = Post.objects.filter(author__name=author_name)
            serializer = PostSerializer(posts, many=True)
        else:
            posts = Post.objects.none()
        return Response(serializer.data)
    def get_posts_by_author_name(self, request, author_name):
        posts = Post.objects.filter(author__name=author_name)
        serializer = PostSerializer(posts, many=True)
        return render(request, 'posts/author_posts.html', {'posts': serializer.data})
    def get_posts_by_author_email(self, request, author_email):
        posts = Post.objects.filter(author__email=author_email)
        serializer = PostSerializer(posts, many=True)
        return render(request, 'posts/author_posts.html', {'posts': serializer.data})