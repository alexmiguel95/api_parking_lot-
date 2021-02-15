from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import LevelSerializer
from .models import Level
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


class LevelView(APIView):
    # Primition by model.
    queryset = Level.objects.none()
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = LevelSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        level = Level.objects.get_or_create(**request.data)[0]
        serializer = LevelSerializer(level)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
