"""
URL configuration for animerecommend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anime.urls', namespace='anime')),
    # path('staff/', include('staff.urls', namespace='staff')),
    # path('anime/', include('anime.urls')),  # Include anime app's urls
    path('user_account/', include('user_account.urls',namespace='user_account')),
    path('api/staff/', include('staff.urls',namespace='staff')),
    path('api/anime/', include('anime.urls',namespace='anime')),
    path('api/recommend/', include('anime.urls',namespace='anime')),
    path('api/staffrecommend/', include('anime.urls',namespace='anime')),



]
