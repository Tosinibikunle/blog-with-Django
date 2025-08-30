from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/article_list.html", {"articles": articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})

# Placeholder views for additional routes
def article_create(request):
    return HttpResponse("Create Article - To be implemented")
def article_edit(request, slug):
    return HttpResponse(f"Edit Article {slug} - To be implemented")
def article_delete(request, slug):
    return HttpResponse(f"Delete Article {slug} - To be implemented")
def article_by_category(request, category):
    return HttpResponse(f"Articles in Category {category} - To be implemented")
def article_search(request):
    return HttpResponse("Search Articles - To be implemented")
