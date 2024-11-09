from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                  # Home page
    path("add-dish/", views.add_dish, name="add_dish"),   # Add dish page
    path("login/", views.new_login, name="new_login"),    # Login page
]
