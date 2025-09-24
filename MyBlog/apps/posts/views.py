from django.shortcuts import render
from .models import Post


# Create your views here.

class PostListView:
    def list(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})
    def detail(self, request, post_id):
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', {'post': post})
    def author_posts(self, request, author_id):
        posts = Post.objects.filter(author_id=author_id)
        return render(request, 'posts/author_posts.html', {'posts': posts})
    def author_name(self, request, author_name):
        posts = Post.objects.filter(author__name=author_name)
        return render(request, 'posts/author_posts.html', {'posts': posts})
    def author_email(self, request, author_email):
        posts = Post.objects.filter(author__email=author_email)
        return render(request, 'posts/author_posts.html', {'posts': posts})