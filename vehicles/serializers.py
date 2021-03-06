from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'id',
            'license_plate',
            'vehicle_type',
            'arrived_at',
            'paid_at',
            'amount_paid',
            'spot',
            'fk_level'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'arrived_at': {'read_only': True},
            'paid_at': {'read_only': True},
            'amount_paid': {'read_only': True},
            'fk_level': {'write_only': True}
        }


class ReleaseVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'license_plate',
            'vehicle_type',
            'arrived_at',
            'paid_at',
            'amount_paid',
            'spot'
        )
        extra_kwargs = {
            'arrived_at': {'read_only': True},
            'paid_at': {'read_only': True},
            'amount_paid': {'read_only': True}
        }
