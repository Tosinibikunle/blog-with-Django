from django.http import HttpResponse


def Homepage(request):
    return HttpResponse('Homepage')

def about(request):
    return HttpResponse('about')

