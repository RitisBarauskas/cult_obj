from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('profile', views.profile, name='profile'),
    path('rg', views.rg, name='rg'),
    path('index2', views.index2, name='index2'),
    path('show', views.show),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]