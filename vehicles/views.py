from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import VehicleSerializer
from .models import Vehicle
from .services.get_data_level import get_data_level


class VehicleView(APIView):
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle = Vehicle.objects.create(**request.data)
        vehicle.paid_at = None
        vehicle.save

        level = get_data_level(vehicle.vehicle_type)

        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
