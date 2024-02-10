from rest_framework import generics
from account.mixins import AdminUserPermissionsMixin
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.response import Response
import base64
from rest_framework import permissions
# Create your views here.

class InventoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

class InventoryAddItemView(AdminUserPermissionsMixin, generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    def post(self, request):
        # create a user
        try:
            print(request.data)
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            print(serializer.validated_data)
            serializer.save()
            return Response({'status': True, 'message' : 'Item added Successfully'}, status =200)
        
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status = 400)
class InventoryListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
class InventoryBreakfastListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category = 'breakfast')
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
class InventoryLunchListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category = 'lunch')
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
class InventoryShakesListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category = 'shakes')
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
class InventoryUpdateAPIView(AdminUserPermissionsMixin, generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDeleteAPIView(AdminUserPermissionsMixin, generics.DestroyAPIView):
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
