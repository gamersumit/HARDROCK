from rest_framework import serializers
from .models import Cart
from account.models import CustomUser
from inventory.models import Inventory

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(write_only = True, queryset=CustomUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(write_only = True, queryset=Inventory.objects.all())
    product_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity', 'product_details']

    def get_product_details(self, obj):
        # Assuming you have a method in your Inventory model to get details
        product = Inventory.objects.get(id=obj.product.id)
        return {
            'name': product.name,
            'content': product.content,
            'image' : product.image or None,
            'price' : product.price,
            # Add more fields as needed
        }