
# accounts/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Favourite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def register_user(request):
    # Extract the data from the request body
    form = UserCreationForm(request.data)

    # Check if the form is valid
    if form.is_valid():
        # Save the user and return a success message
        form.save()
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
    else:
        # Return validation errors
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login_user(request):
    # Get username and password from the request body
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,"message": "Login successful!"}, status=status.HTTP_200_OK)
        # If authentication is successful, log the user in
    else:
        # If authentication fails, return error
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    
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