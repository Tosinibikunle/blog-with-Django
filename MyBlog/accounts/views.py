from django.shortcuts import render
from .import views 
# Create your vi.

def signup_view(request):
    return render(request,'accounts/signup_view.html',name='signup')


def login_view(request):
    return render(request, 'accounts/login_view.html',name='login')
    