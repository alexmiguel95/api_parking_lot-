from django.contrib.auth.models import User 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSeializer
from django.contrib.auth import authenticate


class AccountView(APIView):
    def post(self, request):
        serializer = UserSeializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**request.data)
        serializer = UserSeializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = UserSeializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=request.data["username"],
            password=request.data["password"],
        )

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"message": "Invalid username or password"}, 
            status=status.HTTP_401_UNAUTHORIZED
        )