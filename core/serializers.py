from rest_framework import serializers
from django.forms import ValidationError
from django.contrib.auth import get_user_model
from random import randint
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    
class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError(
                {
                    'confirm_password' : 'Confirm password doesn\'t match with password'
                }
            )
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        otp = randint(0000,9999)
        user.otp = otp
        user.save()
        subject = 'Registration successful'
        request = self.context['request']
        activation_link = f'{request.get_host()}?otp={otp}'
        message = f"""Hi {user.username}, your otp for activating your account is {otp} for {user.email}.
        Your activation link is {activation_link}"""
        email_from = 'hello@newrestro.com'
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        return user

class OTPVerificationSerializer(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.EmailField()
    
    def validate(self,attrs):
       user = User.objects.filter(
            email = attrs['email'],
            otp = attrs['otp'],
        ).exists() 
       if not user:
           raise ValidationError({'details' : 'OTP must be stale or Invalid.'})
       return attrs
    
    def update(self, instance, validated_data):
        instance.is_active = True
        instance.save()  
        
        return instance
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validata_email(self, value):
        user = User.objects.filter(email=value).exists()
        if not user:
            raise ValidationError(
                {
                    'details' : 'User with this email doesn\'t exist'
                }
            )
        return value
    
class PasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    
    def validata_email(self, attrs):
        user = User.objects.filter(email=attrs.get('email'),otp=attrs.get('otp')).exists()
        if not user:
            raise ValidationError(
                {
                    'details' : 'OTP or email is invalid'
                }
            )
        return attrs
    
    def update(self, instance, validated_data):
        instance.password = make_password(
            validated_data.get('password')
        )
        instance.save()
        return instance