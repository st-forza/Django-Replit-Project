from django.urls import path
from . import views

urlpatterns = [
    path("add-dish/", views.add_dish, name="add_dish"),
    path("", views.index, name="index"),
    path("add-dish/", views.add_dish, name="add_dish"),
    path("login/", views.new_login, name="new_login"),

    path('', views.index, name="index"),
    path('add/', views.add_dish, name='add_dish'),
    path('login/', views.new_login, name='new_login'),

    
]


