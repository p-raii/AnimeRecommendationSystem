from django.shortcuts import render, redirect, get_object_or_404
from .models import AnimeData
from user_account.models import Favourite
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimeDataSerializer
import gensim
from django.db.models import Q
from itertools import chain
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def anime_search_api(request):
    search_query = request.GET.get('search', '')  # e.g. ?search=Naruto

    if search_query:
        searched_anime = AnimeData.objects.filter(
            Q(title_english__icontains=search_query) |
            Q(title_romanji__icontains=search_query)
        ).first()

        if not searched_anime:
            return Response({"error": "No anime found with that title."}, status=status.HTTP_404_NOT_FOUND)

        AnimeKeyedVector = gensim.models.KeyedVectors.load("./anime/AnimeKeyedVectors.kv")
        
        similar_anime = AnimeKeyedVector.most_similar(
            positive=[str(searched_anime.id)],
            topn=25,
        )
        similar_anime_ids = [anime[0] for anime in similar_anime]

        # Get the AnimeData objects for those IDs
        similar_anime_qs = AnimeData.objects.filter(id__in=similar_anime_ids)

        # Combine searched anime with similar ones
        posts = AnimeData.objects.filter(id=searched_anime.id) | similar_anime_qs
    else:
        # If no search query, return first 10 as a fallback
        posts = AnimeData.objects.all()[:10]

    # Serialize the queryset
    serializer = AnimeDataSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def post_list(request):
    # Get the search query from URL parameters
    search_query = request.GET.get('search', '')  # Default to an empty string if no search query

    # Filter the posts based on the search query
    if search_query:
        searched_anime = AnimeData.objects.filter(
    Q(title_english__icontains=search_query) |
    Q(title_romanji__icontains=search_query) ).first()

        AnimeKeyedVector = gensim.models.KeyedVectors.load("./anime/AnimeKeyedVectors.kv")

        
        similar_anime=AnimeKeyedVector.most_similar(
                positive=[str(searched_anime.id)],
                topn=25,
            )
        similar_anime_ids=[anime[0] for anime in similar_anime]
        # print(similar_anime_ids)
        similar_anime = AnimeData.objects.filter(id__in=similar_anime_ids)
         # Case-insensitive search
        posts =  AnimeData.objects.filter(id=searched_anime.id) |similar_anime 

        # print (posts)
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

