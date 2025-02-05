from django.urls import path
from . import views
from .views import anime_search_api
from django.contrib import admin

app_name = 'anime'
urlpatterns = [
    path('', views.post_list, name='post_list'),
     path('admin/', admin.site.urls),
    path('add_to_favorites/<int:anime_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:anime_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('search/', anime_search_api, name='anime_search_api'),
]