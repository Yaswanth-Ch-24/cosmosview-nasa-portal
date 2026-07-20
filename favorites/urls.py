from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorites_list, name='favorites'),
    path('add/', views.add_favorite, name='add_favorite'),
    path('remove/<int:index>/', views.remove_favorite, name='remove_favorite'),
]
