from django.shortcuts import render
from rest_framework import viewsets
from .models import Like

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer