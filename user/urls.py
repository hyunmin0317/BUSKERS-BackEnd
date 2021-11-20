# api/urls.py
from django.urls import path, include
from .views import RegistrationAPI, LoginAPI, UserAPI, ProfileListAPI, ProfileDetailAPI, ProfileCreateAPI, ProfileUpdateAPI

urlpatterns = [
    path("signup/", RegistrationAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("user/", UserAPI.as_view()),
    path('profile/create/', ProfileCreateAPI.as_view()),
    path("profile/all/", ProfileListAPI.as_view()),
    path("profile/<str:owner>/", ProfileDetailAPI.as_view()),
    path("profile/<str:owner>/update/", ProfileUpdateAPI.as_view())
]