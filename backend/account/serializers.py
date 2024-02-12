from rest_framework import serializers
from .models import CustomUser
from .utils import Utils

class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length = 8, write_only = True)
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'phone_number',
            'is_admin',
            'is_verified',
        ]
    
    
    
    def validate_password(self, value):
       return Utils.validate_password(value)
    

class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length = 8, write_only = True)
    class Meta:
        model = CustomUser
        fields = ['password']
    
    def validate_password(self, value):
       return Utils.validate_password(value)
    

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, write_only=True, required=True, allow_null=False, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False)
    is_admin = serializers.BooleanField(required=True, allow_null=False)

