# api/urls.py
from django.urls import path, include
from .views import RegistrationAPI, LoginAPI, UserAPI, ProfileListAPI

urlpatterns = [
    path("signup/", RegistrationAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("user/", UserAPI.as_view()),
    path("profile/", ProfileListAPI.as_view())
]