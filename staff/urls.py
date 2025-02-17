from django.urls import path
from . import views
from .views import get_all_staff_api
from .views import search_list
from django.contrib import admin

app_name = 'staff'
urlpatterns = [

    path('search/', search_list, name='search_list'),

    path('', get_all_staff_api, name='get_all_staff_api'),

]