from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import VehicleSerializer, ReleaseVehicleSerializer
from .models import Vehicle
from .services.check_free_space import check_free_space
from .services.calculate_payment import get_payment
from django.core.exceptions import ObjectDoesNotExist


class VehicleView(APIView):
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle = Vehicle.objects.create(**request.data)
        spot = check_free_space(vehicle.vehicle_type)

        # There are no vacancies or there is no level registered in the system
        if not spot:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Fill the spot field with vacancy information
        vehicle.spot = spot
        vehicle.fk_level = spot["id"]
        vehicle.save()
        vehicle.paid_at = None

        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, vehicle_id=""):
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except ObjectDoesNotExist:
            return Response(
               {
                   "message":
                       f"Veicle id {vehicle_id} not exist"
               },
               status=status.HTTP_404_NOT_FOUND
            )

        # Release vehicle
        # Update object
        vehicle.spot = None
        vehicle.amount_paid = get_payment(
            vehicle.arrived_at,
            vehicle.paid_at,
            vehicle.fk_level,
            vehicle.vehicle_type
        )
        vehicle.fk_level = None
        vehicle.save()

        serializer = ReleaseVehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)
