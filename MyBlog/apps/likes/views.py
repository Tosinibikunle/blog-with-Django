from django.shortcuts import render
from rest_framework import viewsets
from .models import Like
from .serializers import LikeSerializer, LikeCreateSerializer

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

class LikeDeleteView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_destroy(self, instance):
        instance.delete()

class LikeListViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post_id=post_id)        