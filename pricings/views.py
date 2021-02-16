# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .serializers import PricingSerializer
# from .models import Pricing
# from rest_framework.permissions import DjangoModelPermissions
# from rest_framework.authentication import TokenAuthentication


# class LevelView(APIView):
#     # Primition by model. Only users who are in the Admin permission group can
#     # access.
#     queryset = Pricing.objects.none()
#     permission_classes = [DjangoModelPermissions]
#     authentication_classes = [TokenAuthentication]

#     def post(self, request):
#         serializer = PricingSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         pricing = Pricing.objects.create(**request.data)
#         serializer = PricingSerializer(pricing)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
