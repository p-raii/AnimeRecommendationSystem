# serializers.py
from rest_framework import serializers
from .models import AnimeData
from staff.models import StaffData


class AnimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeData
        fields = '__all__'  # This will include all fields from the AnimeData model

class StaffDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffData
        fields = '__all__'