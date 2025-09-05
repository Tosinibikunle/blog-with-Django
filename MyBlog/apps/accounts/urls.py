
from django.urls import path, include
from django.contrib import admin
from .models import CustomBlogger, customReader
from rest_framework.routers import DefaultRouter
from .views import CustomBloggerViewSet, CustomReaderViewSet, CustomBloggerDetailViewSet

router = DefaultRouter()
router.register(r'bloggers', CustomBloggerViewSet, basename='bloggers')
router.register(r'readers', CustomReaderViewSet, basename='readers')
router.register(r'blogger-detail', CustomBloggerDetailViewSet, basename='blogger-detail')

urlpatterns = [
    path('', include(router.urls)),
]


