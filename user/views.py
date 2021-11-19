# api/views.py
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, ProfileSerializer, ProfileCreateSerializer
from .models import Profile

class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        # if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
        #     body = {"message": "short field"}
        #     return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response(
            {
                "username": user.username,
                "token": token
            }
        )

class LoginAPI(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProfileListAPI(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPI(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreateAPI(CreateAPIView):
    serializer_class = ProfileCreateSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.username)

class ProfileUpdateAPI(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.username)