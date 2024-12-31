
# accounts/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Favourite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout




# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_account:login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'user_account/register.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            auth_login(request, user)  # Log the user in

            # Redirect to the anime list page (or wherever you want to go after login)
            return render(request, 'anime/post_list.html', {'user': user})  # Make sure you have 'anime_list' URL configured
            
    else:
        form = AuthenticationForm()

    return render(request, 'user_account/login.html', {'form': form})
   

# def favourite(request):
#     favorites = Favourite.objects.filter(user=request.user)
#     return render(request, 'user_account/favorites_list.html', {'favorites': favorites})

# accounts/views.py

@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    # Get the list of favorite anime for the logged-in user
    favorites = Favourite.objects.filter(user=user)
    
    # Pass user info and favorites to the template
    return render(request, 'user_account/profile.html', {'user': user, 'favorites': favorites})

def logout_view(request):
    logout(request)  # This logs the user out
    return redirect('anime:post_list') 