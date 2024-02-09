from rest_framework import serializers
from .models import Cart
from account.models import CustomUser
from inventory.models import Inventory

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Inventory.objects.all())
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity']
    
    