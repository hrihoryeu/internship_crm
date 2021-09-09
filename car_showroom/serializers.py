from rest_framework import serializers

from .models import CarShowroom, CarShowroomSale, CarShowroomCustomer, CarShowroomCar


class CarShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroom
        fields = '__all__'


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
