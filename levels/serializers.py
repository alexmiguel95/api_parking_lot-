from rest_framework import serializers
from .models import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            'id',
            'name',
            'fill_priority',
            'available_spots',
            'bike_spots',
            'car_spots'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'car_spots': {'write_only': True},
            'bike_spots': {'write_only': True}
        }
