from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('verify/', UserVerificationAPIView.as_view(), name='user_verification'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('forgot_password/', UserForgotPasswordAPIView.as_view(), name='user_forgot_password'),
    path('reset_password/', UserResetPasswordAPIView.as_view(), name='user_reset_password'),
]