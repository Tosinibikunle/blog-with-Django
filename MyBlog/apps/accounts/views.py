from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .models import CustomBlogger, customReader
from .serializers import CustomBloggerSerializer, CustomBloggerCreateSerializer, CustomReaderSerializer, CustomReaderCreateSerializer
from rest_framework.response import Response
from rest_framework import status


User = get_user_model()

class CustomBloggerViewSet(viewsets.ModelViewSet):
    queryset = CustomBlogger.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CustomBloggerCreateSerializer
        return CustomBloggerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()

class CustomReaderViewSet(viewsets.ModelViewSet):
    queryset = customReader.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CustomReaderCreateSerializer
        return CustomReaderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()

class CustomBloggerDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomBlogger.objects.all()
    serializer_class = CustomBloggerSerializer
    permission_classes = [permissions.IsAuthenticated]    