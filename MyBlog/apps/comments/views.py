from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer, CommentCreateSerializer
from rest_framework import generics, permissions

# Create your views here.

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)