from rest_framework import serializers
from .models import User, Product, Publication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'email')
    # username = serializers.CharField(max_length=100)
    # phone = serializers.CharField(max_length=8)
    # email = serializers.EmailField(max_length=254)

    # def create(self, validated_data):
    #     return User.objects.create(validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'publication', 'name', 'price')

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'title', 'user', 'product', 'latitud', 'longitud', 'date_time', 'comments')