from django.http import HttpResponse
from django.shortcuts import render


def Homepage(request):
    # return HttpResponse('Homepage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

