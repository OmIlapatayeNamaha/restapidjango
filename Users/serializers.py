from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class UserVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

class UserForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()   