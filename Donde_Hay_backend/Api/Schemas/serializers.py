from rest_framework import serializers
from ..Models.models import User, Product, SalePlace, Location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "phone", "email"]


class UserSearchSerializer(serializers.Serializer):
    field = serializers.ChoiceField(choices=["username", "phone", "email"])
    value = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "salePlace"]


class SalePlaceSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SalePlace
        fields = ["id", "name", "location", "products"]


class LocationSerializer(serializers.ModelSerializer):
    salePlace = SalePlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ["id", "latitud", "longitud", "direction", "salePlace"]
