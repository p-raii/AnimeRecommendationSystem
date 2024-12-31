from django.shortcuts import render, redirect, get_object_or_404
from .models import AnimeData
from user_account.models import Favourite
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimeDataSerializer

# Create your views here.
def post_list(request):
    # Get the search query from URL parameters
    search_query = request.GET.get('search', '')  # Default to an empty string if no search query

    # Filter the posts based on the search query
    if search_query:
        posts = AnimeData.objects.filter(title_english__icontains=search_query)  # Case-insensitive search
    else:
        posts = AnimeData.objects.all()[:10]  # Display all if no search query, with limit to 10 posts

    return render(request, 'anime/post_list.html', {'posts': posts, 'search_query': search_query})

# # Create your views here.
# def post_list(request):
#     posts = AnimeData.objects.all()[:10]

#     return render(request, 'anime/post_list.html', {'posts': posts})

def add_to_favorites(request, anime_id):
    anime = get_object_or_404(AnimeData, id=anime_id)
    Favourite.objects.get_or_create(user=request.user, anime=anime)  # Add to favorites
    return redirect('anime_list')  # Redirect to the anime list

def remove_from_favorites(request, anime_id):
    anime = get_object_or_404(AnimeData, id=anime_id)
    Favourite.objects.filter(user=request.user, anime=anime).delete()  # Remove from favorites
    return redirect('favorites_list')  # Redirect to favorites list

# views.py


class AnimeDataList(APIView):
    def get(self, request):
        anime_data = AnimeData.objects.all()  # Get all anime data
        serializer = AnimeDataSerializer(anime_data, many=True)
        return Response(serializer.data)  # Return serialized data

    def post(self, request):
        serializer = AnimeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save new AnimeData instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
