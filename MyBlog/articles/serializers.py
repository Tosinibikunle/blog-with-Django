from .admin import ArticleAdmin
from django.db import models 
from rest_framework import serializers
from .models import Article
from django.utils.text import slugify
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=Article.objects.all())]
    )
    slug = serializers.SlugField(required=False)  # Slug will be auto-generated
    body = serializers.CharField()
    date = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    thumb = serializers.ImageField(required=False, allow_null=True)
    category = serializers.ChoiceField(choices=Article.CATEGORY_CHOICES, required=False, allow_blank=True)
    is_published = serializers.BooleanField(default=True)
    views = serializers.IntegerField(read_only=True)  # Read-only field for views
    likes = serializers.IntegerField(read_only=True)  # Read-only field for likes

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'body', 'date', 'updated_at', 'thumb', 'category', 'is_published', 'views', 'likes']

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data and (not instance.slug or instance.title != validated_data['title']):
            validated_data['slug'] = slugify(validated_data['title'])
        return super().update(instance, validated_data)