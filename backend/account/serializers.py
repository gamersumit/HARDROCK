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
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    email = serializers.EmailField()
    is_admin = serializers.BooleanField()


    def validate(self, attrs):
        password = attrs.get('password', None)
        email = attrs.get('email', None)
        is_admin = attrs.get('is_admin', None)

        if (email is None) or (password is None) or (is_admin is None) :
            raise serializers.ValidationError("Missing Fields")

        return attrs
