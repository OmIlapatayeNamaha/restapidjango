from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from .serializers import *

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserVerificationAPIView(APIView):
    def post(self, request):
        serializer = UserVerificationSerializer(data=request.data)
        # Add verification logic here
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email)
                # Perform OTP verification logic here
                # If verification successful:
                return Response("Verification Successful", status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Verification Successful", status=status.HTTP_200_OK)

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        # Add login logic here
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            user = authenticate(email=email, otp=otp)
            if user:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = UserForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                # Generate and send OTP for password reset via email
                # Implement OTP generation and sending email logic here
                return Response("Password reset link sent", status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserResetPasswordAPIView(APIView):
    def post(self, request):
        serializer = UserResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email)
                # Validate OTP and reset password logic here
                return Response("Password reset successful", status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

