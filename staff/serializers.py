# serializers.py
from rest_framework import serializers
from .models import StaffData

class StaffDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffData
        fields = '__all__'  # This will include all fields from the AnimeData model
