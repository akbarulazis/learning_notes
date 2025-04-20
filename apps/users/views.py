
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'users/login.html')

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/login')
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            Profile.objects.create(user=user)
        
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('/login')
        else:
            messages.error(request, "Registration failed. Please check the form.")
            return render(request, 'users/register.html', {'form': form})

def logout_view(request):
 
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')

@login_required
def profile(request):
   
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)