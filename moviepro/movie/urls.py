"""
URL configuration for moviepro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from movie import views
from django.urls import path
app_name='movie'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('deletebyid/<int:p>', views.deletemoviebyid, name='deletemoviebyid'),
    path('editbyid/<int:p>', views.editmoviebyid, name='editmoviebyid'),
    path('view1/<int:p>', views.viewmoviebyid, name='viewmoviebyid'),
    path('add/', views.addmovie, name='addmovie'),



]
