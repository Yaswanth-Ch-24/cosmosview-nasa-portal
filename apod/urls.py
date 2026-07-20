from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apod/<str:date_str>/', views.apod_date, name='apod_date'),
]
