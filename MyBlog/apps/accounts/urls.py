
from django.urls import path, include
from django.contrib import admin
from .models import CustomBlogger, customReader
from rest_framework.routers import DefaultRouter
from .views import CustomBloggerViewSet, CustomReaderViewSet, CustomBloggerDetailViewSet

router = DefaultRouter()
router.register(r'bloggers', CustomBloggerViewSet)
router.register(r'readers', CustomReaderViewSet)
router.register(r'blogger-detail', CustomBloggerDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


