from django.urls import path
from . import views
from .views import get_all_staff_api

from django.contrib import admin

app_name = 'staff'
urlpatterns = [

    path('', get_all_staff_api, name='get_all_staff_api'),

]