# api/urls.py
from django.urls import path
from .views import CreateAPI, ListAPI, MyListAPI, DetailAPI, DeleteAPI, UpdateAPI

urlpatterns = [
    path('all/', ListAPI.as_view()),
    path('create/', CreateAPI.as_view()),
    path('mylist/', MyListAPI.as_view()),
    path('<int:pk>/', DetailAPI.as_view()),
    path('<int:pk>/update/', UpdateAPI.as_view()),
    path('<int:pk>/delete/', DeleteAPI.as_view())
]