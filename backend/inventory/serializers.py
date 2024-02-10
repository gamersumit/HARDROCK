# serializers.py
from rest_framework import serializers
from .models import Inventory
# from drf_extra_fields.fields import Base64ImageField
import base64
from django.core.files.base import ContentFile


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'content', 'price', 'quantity', 'category', 'image']

    
    def validate_category(self, value):
        if not value :
            raise serializers.ValidationError("Empty category")
        
        else :
            value = value.lower() 
            if(value not in ['breakfast', 'lunch',  'shakes']) :
               raise serializers.ValidationError("Invalid category")
            return value