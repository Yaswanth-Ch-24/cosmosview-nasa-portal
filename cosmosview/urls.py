from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apod.urls')),
    path('mars/', include('mars_rover.urls')),
    path('favorites/', include('favorites.urls')),
]
