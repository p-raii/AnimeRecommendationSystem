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
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.




@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_staff_api( request):
    staff_data = StaffData.objects.all()  # Get all staff data
    serializer = StaffDataSerializer(staff_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data
