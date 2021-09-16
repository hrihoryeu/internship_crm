from rest_framework import serializers

from core.api.v1.serializers import LocationSerializer
from core.models import Location

from car_showroom.models import (
    CarShowroom,
    CarShowroomSale,
    CarShowroomCustomer,
    CarShowroomCar,
)


class CarShowroomSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True)

    class Meta:
        model = CarShowroom
        fields = '__all__'

    def create(self, validated_data):
        locations_data = validated_data.pop('location')
        car_showroom = CarShowroom.objects.create(**validated_data)
        print(f'valdata - {validated_data}')
        print(f'location data - {locations_data}')
        for location_data in locations_data:
            Location.objects.create(car_showroom=car_showroom, **location_data)
        return car_showroom


class CarShowroomSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomSale
        fields = '__all__'


class CarShowroomCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomCustomer
        fields = '__all__'


class CarShowroomCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomCar
        fields = '__all__'
