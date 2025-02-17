from django.shortcuts import render, redirect, get_object_or_404
from .models import StaffData
from user_account.models import Favourite
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StaffDataSerializer
import gensim
from django.db.models import Q
from itertools import chain
from rest_framework.decorators import api_view
# Create your views here.




@api_view(['GET'])
def get_all_staff_api( request):
    staff_data = StaffData.objects.all()  # Get all staff data
    serializer = StaffDataSerializer(staff_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data


# @api_view(['GET'])
# def staff_search_api(request):
#     search_query = request.GET.get('search', '')  # e.g. ?search=Naruto

#     if search_query:
#         searched_staff = StaffData.objects.filter(
#             Q(title_english__icontains=search_query) |
#             Q(title_romanji__icontains=search_query)
#         ).first()

#         if not searched_staff:
#             return Response({"error": "No staff found with that title."}, status=status.HTTP_404_NOT_FOUND)

#         staffKeyedVector = gensim.models.KeyedVectors.load("./staff/staffKeyedVectors.kv")
        
#         similar_staff = staffKeyedVector.most_similar(
#             positive=[str(searched_staff.id)],
#             topn=25,
#         )
#         similar_staff_ids = [staff[0] for staff in similar_staff]

#         # Get the staffData objects for those IDs
#         similar_staff_qs = StaffData.objects.filter(id__in=similar_staff_ids)

#         # Combine searched staff with similar ones
#         posts = StaffData.objects.filter(id=searched_staff.id) | similar_staff_qs
#     else:
#         # If no search query, return first 10 as a fallback
#         posts = StaffData.objects.all()[:10]

#     # Serialize the queryset
#     serializer = StaffDataSerializer(posts, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

def search_list(request):

    search_query = request.GET.get('search', '')  # Default to an empty string if no search query

    # Filter the posts based on the search query
    if search_query:
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
        posts =  StaffData.objects.filter(id=searched_staff.id) |similar_staff 

        # print (posts)
    else:
        posts = StaffData.objects.all()[:10]  # Display all if no search query, with limit to 10 posts

    return render(request, 'anime/post_list.html', {'posts': posts, 'search_query': search_query})