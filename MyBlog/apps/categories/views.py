from django.shortcuts import render
from.models import Category, Tag


class CategoryViewset():
    def list(self, request):
        categories = Category.objects.all()
        return render(request, 'categories/category_list.html', {'categories': categories})

class TagViewset():
    def list(self, request):
        tags = Tag.objects.all()
        return render(request, 'categories/tag_list.html', {'tags': tags})