from rest_framework import generics
from account.mixins import AdminUserPermissionsMixin
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.response import Response
from .inventory_utils import InvUtils
from rest_framework import permissions
from rest_framework.views import APIView

# Create your views here.

#to get a perticular item from inventory
class InventoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

# to add item to inventory
class InventoryAddItemView( generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def post(self, request):
        try:
            # convert base64_image to raw image
            image_base64 = request.data.pop('image')
            image = InvUtils.base64_to_image(image_base64, request.data['image_name'])

            # update raw data
            request.data['image'] = image

            # serialize data
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()

            #return response
            return Response({'status': True, 'message' : 'Item added Successfully'}, status =200)
           
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status = 400)

# to get all the items from inventory/menu
class InventoryListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

# to get items only releated to breakfast
    
# class YourListView(APIView):
#     def get(self, request):
#     # Filter the queryset to include only the particular items you want
#     queryset = Inventory.objects.filter(category='breakfast')

#     # Serialize the filtered queryset
#     serializer = YourModelSerializer(queryset, many=True)

#     return Response(serializer.data)
class InventoryBreakfastListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Inventory.objects.filter(category='breakfast')
    serializer_class = InventorySerializer
    


# to get items only releated to lunch
class InventoryLunchListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category='lunch')
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    

# to get items only releated to shakes
class InventoryShakesListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.filter(category='shakes')
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    
   

# to update item fields
class InventoryUpdateAPIView(AdminUserPermissionsMixin, generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# to delete an item from inventory
class InventoryDeleteAPIView(AdminUserPermissionsMixin, generics.DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


#shortnaming
inventory_create_view = InventoryAddItemView.as_view()
inventory_detail_view = InventoryDetailAPIView.as_view()
inventory_list_view =   InventoryListAPIView.as_view()
inventory_breakfast_list_view =   InventoryBreakfastListAPIView.as_view()
inventory_shakes_list_view =   InventoryShakesListAPIView.as_view()
inventory_lunch_list_view =   InventoryLunchListAPIView.as_view()
inventory_update_view = InventoryUpdateAPIView.as_view()
inventory_delete_view = InventoryDeleteAPIView.as_view()
