from rest_framework import serializers
from .models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ['anime', 'user']  # Only need these two fields
        extra_kwargs = {'user': {'read_only': True}}  # Prevent user from modifying it

    def validate(self, data):
        user = self.context['request'].user
        anime = data['anime']

        # Check if already in favorites
        if Favourite.objects.filter(user=user, anime=anime).exists():
            raise serializers.ValidationError("Anime is already in favorites!")
        
        return data