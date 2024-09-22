from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("myrestaurant.urls")),
    path("", include("myrestaurant.urls")),
    path("", include("myrestaurant.urls")),
    path('admin/', admin.site.urls),
    path('', include('myrestaurant.urls')),  # Root URL should point to myrestaurant.urls
]


# python manage.py startapp myrestaurant