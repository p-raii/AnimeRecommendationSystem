from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User



# Create your models here.
class AnimeData(models.Model):
        # Define the fields as before
    title_english = models.CharField(max_length=255, blank=True, null=True)
    title_romanji = models.CharField(max_length=255, blank=True, null=True)
    title_native = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    trailer = models.CharField(max_length=255, blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    staff = models.TextField(blank=True, null=True)
    studio = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(max_length=200,blank=True, null=True)

    # Explicitly set the 'id' field without auto incrementing
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'anime_data'
    
    def __str__(self):
        return self.title_english if self.title_english else self.title_native
# from django.db import models
# from anime.models import Anime

# class Favourite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     anime = models.ForeignKey(AnimeData, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.username} - {self.anime.title_english}"
