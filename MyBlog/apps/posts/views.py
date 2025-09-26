from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post




class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})

class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'posts/post_detail.html', {'post': post})
    def get_author_posts(self, request, author_id):
        posts = Post.objects.filter(author_id=author_id)
        return render(request, 'posts/author_posts.html', {'posts': posts})
    def get_author_name_posts(self, request, author_name):
        posts = Post.objects.filter(author__name=author_name)
        return render(request, 'posts/author_posts.html', {'posts': posts})    
class PostAuthorView(View):
    def get(self, request, author_id=None, author_name=None):
        if author_id:
            posts = Post.objects.filter(author_id=author_id)
        elif author_name:
            posts = Post.objects.filter(author__name=author_name)
        else:
            posts = Post.objects.none()
        return render(request, 'posts/author_posts.html', {'posts': posts})
    def get_posts_by_author_name(self, request, author_name):
        posts = Post.objects.filter(author__name=author_name)
        return render(request, 'posts/author_posts.html', {'posts': posts})
    def get_posts_by_author_email(self, request, author_email):
        posts = Post.objects.filter(author__email=author_email)
        return render(request, 'posts/author_posts.html', {'posts': posts})