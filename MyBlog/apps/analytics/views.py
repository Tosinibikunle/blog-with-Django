from django.shortcuts import render
from .models import PageView, ClickEvent
from .serializers import PageViewSerializer, ClickEventSerializer
from rest_framework import generics


class PageViewList(generics.ListCreateAPIView):
    queryset = PageView.objects.all()
    serializer_class = PageViewSerializer

class ClickEventList(generics.ListCreateAPIView):
    queryset = ClickEvent.objects.all()
    serializer_class = ClickEventSerializer
