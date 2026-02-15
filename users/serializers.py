from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
