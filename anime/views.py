from django.shortcuts import render, redirect, get_object_or_404
from .models import AnimeData
from staff.models import StaffData
from user_account.models import Favourite
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimeDataSerializer
from .serializers import StaffDataSerializer
import gensim
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.




@api_view(['GET'])
def get_all_anime_api( request):
    anime_data = AnimeData.objects.all()  # Get all anime data
    serializer = AnimeDataSerializer(anime_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def anime_search_api(request):
    search_query = request.GET.get('search', '')  # e.g. ?search=Naruto

    if search_query:
        

        searched_anime = AnimeData.objects.filter(
            Q(title_english__icontains=search_query) |
            Q(title_romanji__icontains=search_query)
        ).first()

        
        if searched_anime:        

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

        if not searched_anime:
            searched_staff = StaffData.objects.filter(
        Q(name_full__icontains=search_query) |
        Q(name_native__icontains=search_query) ).first()

            staffKeyedVector = gensim.models.KeyedVectors.load("./staff/StaffKeyedVectors60.kv")

            
            similar_staff=staffKeyedVector.most_similar(
                    positive=[str(searched_staff.id)],
                    topn=25,
                )
            similar_staff_ids=[staff[0] for staff in similar_staff]
            # print(similar_staff_ids)
            similar_staff = StaffData.objects.filter(id__in=similar_staff_ids)
            # Case-insensitive search
            posts=  StaffData.objects.filter(id=searched_staff.id) |similar_staff 
            serializer = StaffDataSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)




    else:
        # If no search query, return first 10 as a fallback
        posts = AnimeData.objects.all()[:10]

    # Serialize the queryset
    serializer = AnimeDataSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



def post_list(request):
    # Get the search query from URL parameters
    # search_query = request.GET.get('q', '')

    # if not search_query:
    #     return render(request, 'anime/post_list.html', {'posts': []})

    # results = trie.search_prefix(search_query)  # Get matching titles from Trie
    # anime_list = AnimeData.objects.filter(
    # Q(title_english__in=results) | Q(title_romanji__in=results))
    # return render(request, 'anime/post_list.html', {'posts': anime_list, 'search_query': search_query})

    search_query = request.GET.get('search', '')  # Default to an empty string if no search query

    # Filter the posts based on the search query
    if search_query:
        searched_anime = AnimeData.objects.filter(
    Q(title_english__icontains=search_query) |
    Q(title_romanji__icontains=search_query) ).first()

        if searched_anime:
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
        elif not searched_anime:
            searched_staff = StaffData.objects.filter(
        Q(name_full__icontains=search_query) |
        Q(name_native__icontains=search_query) ).first()

            staffKeyedVector = gensim.models.KeyedVectors.load("./staff/StaffKeyedVectors60.kv")

            
            similar_staff=staffKeyedVector.most_similar(
                    positive=[str(searched_staff.id)],
                    topn=25,
                )
            similar_staff_ids=[staff[0] for staff in similar_staff]
            # print(similar_staff_ids)
            similar_staff = StaffData.objects.filter(id__in=similar_staff_ids)
            # Case-insensitive search
            postss =  StaffData.objects.filter(id=searched_staff.id) |similar_staff 
            return render(request, 'anime/post_list.html', {'postss': postss, 'search_query': search_query})

        # print (posts)  # Display all if no search query, with limit to 10 posts


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



