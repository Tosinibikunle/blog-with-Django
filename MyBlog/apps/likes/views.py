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