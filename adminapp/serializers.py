from asyncore import write
from pyexpat import model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import *
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':"password"}
                                      ,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email','password','password2','name','tc']
        extra_kwargs = {
            "password":{"write_only":True}
        }
        
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm_password doesn't match")
        return attrs

    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)
            
            
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomUser
        fields = ['email','password']
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username','email','address']
        