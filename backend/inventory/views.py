from django.shortcuts import render
from rest_framework import generics
from account.mixins import AdminUserPermissionsMixin
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.response import Response
import base64
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

class InventoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryAddItemView(generics.GenericAPIView):
    serializer_class = InventorySerializer

    def post(self, request):
        # create a user
        try :
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            item = serializer.save()
            # return Response({'status': True, 'message' : 'Item added Successfully'}, status =200)
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status = 400)

        try :  
            img = request.POST.get('img_source')
            format, imgstr = img.split(';base64,')
            base64.b64decode(imgstr)
            item.img_source = request.data
            item.save()
            return Response({'status': True, 'message' : 'Registration Successful'}, status =200)
        except:
            return Response({'status': True, 'message' : 'Registration Successful'}, status =200)
        
class InventoryListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    pagination_class = LimitOffsetPagination

class InventoryBreakfastListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category = 'breakfast')
    serializer_class = InventorySerializer
    pagination_class = LimitOffsetPagination

class InventoryLunchListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category = 'lunch')
    serializer_class = InventorySerializer
    pagination_class = LimitOffsetPagination

class InventoryShakesListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category = 'shakes')
    serializer_class = InventorySerializer
    pagination_class = LimitOffsetPagination
class InventoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


#shortnaming
inventory_create_view = InventoryAddItemView.as_view()
inventory_detail_view = InventoryDetailAPIView.as_view()
inventory_list_view =   InventoryListAPIView.as_view()
inventory_breakfast_list_view =   InventoryListAPIView.as_view()
inventory_shakes_list_view =   InventoryListAPIView.as_view()
inventory_lunch_list_view =   InventoryListAPIView.as_view()
inventory_update_view = InventoryUpdateAPIView.as_view()
inventory_delete_view = InventoryDeleteAPIView.as_view()
