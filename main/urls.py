from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('profile/', views.profile, name='profile'),
    path('rg/', views.rg, name='rg'),
    path('search_objects/', views.search_objects, name='search_objects'),
    path('show/', views.show, name='show'),
    path('accounts/', include('django.contrib.auth.urls')),
]
