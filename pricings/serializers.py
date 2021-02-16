from rest_framework import serializers


class PricingSerializer(serializers.Serializer):
    a_coefficient = serializers.IntegerField()
    b_coefficient = serializers.IntegerField()
