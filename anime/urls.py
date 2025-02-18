from django.urls import path
from . import views
from .views import anime_search_api
from .views import get_all_anime_api,anime_recommend, staff_recommend
from django.contrib import admin

app_name = 'anime'
urlpatterns = [
    path('', views.post_list, name='post_list'),
     path('admin/', admin.site.urls),
    path('add_to_favorites/<int:anime_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:anime_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('api/search/', anime_search_api, name='anime_search_api'),
    path('api/anime/', get_all_anime_api, name='get_all_anime_api'),
    path('api/recommend/', anime_recommend, name='anime_recommend'),
    path('api/staffrecommend/', staff_recommend, name='staff_recommend'),


]