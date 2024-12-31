from django.urls import path
from . import views
from .views import AnimeDataList

app_name = 'anime'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add_to_favorites/<int:anime_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:anime_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('api/anime/', AnimeDataList.as_view(), name='anime-list'),
]