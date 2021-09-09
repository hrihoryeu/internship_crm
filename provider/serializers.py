from rest_framework import serializers

from .models import Car, Provider, ProviderCar, ProviderSale


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCar
        fields = '__all__'


class ProviderSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderSale
        fields = '__all__'
