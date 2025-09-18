from django.shortcuts import render
from rest_framework import viewsets
from .models import Like
from .serializers import LikeSerializer, LikeCreateSerializer
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.response import Response

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return LikeCreateSerializer
        return super().get_serializer_class()
    
class LikeCreateViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

class LikeDeleteView(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_destroy(self, instance):
        instance.delete()

class LikeListViewSet(ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post_id=post_id)

class LikeCountView(ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post_id=post_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = queryset.count()
        return Response({'post_id': self.kwargs['post_id'], 'like_count': count})