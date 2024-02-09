from django.shortcuts import render
from rest_framework import generics
from account.mixins import AdminUserPermissionsMixin
from .models import Inventory
from .serializers import CartSerializer
from rest_framework.response import Response
import base64
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
# # Create your views here.

# class InventoryDetailAPIView(generics.RetrieveAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer

class CartAddItemView(generics.GenericAPIView):
    serializer_class = CartSerializer

    def post(self, request):
        # create a user
        try :
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({'status': True, 'message' : 'Item added Successfully'}, status =200)
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status = 400)

      
# class InventoryListAPIView(generics.ListAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer
#     pagination_class = LimitOffsetPagination

# class InventoryUpdateAPIView(generics.UpdateAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer

# class InventoryDeleteAPIView(generics.DestroyAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer


# #shortnaming
cart_add_view = CartAddItemView.as_view()
# inventory_detail_view = InventoryDetailAPIView.as_view()
# inventory_list_view =   InventoryListAPIView.as_view()
# inventory_update_view = InventoryUpdateAPIView.as_view()
# inventory_delete_view = InventoryDeleteAPIView.as_view()
