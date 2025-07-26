# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
                    if form.is_valid():
                                user = form.save()
                                            login(request, user)  # Automatically log the user in after signup
                                                        messages.success(request, 'Signup successful. You are now logged in.')
                                                                    return redirect('home')  # Replace 'home' with the name of your home URL
                                                                            else:
                                                                                        messages.error(request, 'Signup failed. Please check the errors below.')
                                                                                            else:
                                                                                                    form = UserCreationForm()
                                                                                                        return render(request, 'account/signup_view.html', {'form': form})


                                                                                                        def login_view(request):
                                                                                                            if request.method == 'POST':
                                                                                                                    form = AuthenticationForm(request, data=request.POST)
                                                                                                                            if form.is_valid():
                                                                                                                                        user = form.get_user()
                                                                                                                                                    login(request, user)
                                                                                                                                                                messages.success(request, 'Login successful.')
                                                                                                                                                                            return redirect('home')  # Replace 'home' with the name of your home URL
                                                                                                                                                                                    else:
                                                                                                                                                                                                messages.error(request, 'Login failed. Please check your credentials.')
                                                                                                                                                                                                    else:
                                                                                                                                                                                                            form = AuthenticationForm()
                                                                                                                                                                                                                return render(request, 'account/login_view.html', {'form': form})