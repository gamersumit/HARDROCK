# serializers.py
from rest_framework import serializers
from .models import Inventory
import base64

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'content', 'price', 'quantity', 'category']

    
    def validate_category(self, value):
        if not value :
            raise serializers.ValidationError("Empty category")
        
        else :
            value = value.lower()
            
            if(value not in ['breakfast', 'lunch',  'shakes']) :
               raise serializers.ValidationError("Invalid category")
            
            return value


    # def validate_img_Source(self, img):
    #     if not img :
    #         return None

    #     try:
    #     # Split the Base64 data from the prefix
    #         format, imgstr = img.split(';base64,')
    #     # Decode the Base64 data
    #         base64.b64decode(imgstr)
    #         return imgstr
        
    #     except :
    #         raise serializers.ValidationError("something wrong with image")