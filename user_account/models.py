from django.db import models
from django.contrib.auth.models import User
from anime.models import AnimeData
# Create your models here.
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(AnimeData, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.anime.title_english}"