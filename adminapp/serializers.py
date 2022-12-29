from rest_framework import serializers
from .models import *
class UserRegistrationSerialzier(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        
    def validate(self,attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("password and confirm_password doesn't match")
        return attrs
    
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['email','password']
