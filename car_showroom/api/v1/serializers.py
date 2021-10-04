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
        for location_data in locations_data:
            Location.objects.create(car_showroom=car_showroom, **location_data)
        return car_showroom

    def update(self, instance, validated_data):
        locations_data = validated_data.pop('location')
        locations = (instance.location).all()
        locations = list(locations)
        instance.title = validated_data.get('title', instance.title)
        instance.specs = validated_data.get('specs', instance.specs)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.unique_customers = validated_data.get('unique_customers', instance.unique_customers)
        instance.save()
        for location_data in locations_data:
            location = locations.pop(0)
            location.car_showroom = location_data.get('car_showroom', location.car_showroom)
            location.country = location_data.get('country', location.country)
            location.city = location_data.get('city', location.city)
            location.street = location_data.get('street', location.street)
            location.building_number = location_data.get('building_number', location.building_number)
            location.index = location_data.get('index', location.index)
            location.save()
        return instance


class CarShowroomSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomSale
        fields = '__all__'


class CarShowroomCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomCustomer
        fields = '__all__'


class CarShowroomCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarShowroomCar
        fields = '__all__'
