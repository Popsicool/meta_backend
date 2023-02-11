# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length =65, min_length=8, write_only=True)
#     email = serializers.EmailField(max_length=255, min_length=4)
#     first_name = serializers.CharField(max_length=255, min_length=2)
#     last_name = serializers.CharField(max_length=255, min_length=2)

#     class Meta:
#         model = User
#         fields= ["username", "first_name", "last_name", "email", "password"]
    
#     def validate(self, attrs):
#         email= attrs.get("email", "")
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError(
#                 {"email": "Email already exists"}
#             )
#         return super().validate(attrs)
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=65, min_length=8, write_only=True)
#     username = serializers.CharField(max_length=255, min_length=2)

#     class Meta:
#         model = User
#         fields = ['username', 'password']

from rest_framework import serializers
from .models import Booking, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()
    class Meta:
        model = MenuItem
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    no_of_guests = serializers.IntegerField()
    booking_date = serializers.DateField()
    class Meta:
        model = Booking
        fields = "__all__"
