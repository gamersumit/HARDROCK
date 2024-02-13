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
class InventoryAddItemView(AdminUserPermissionsMixin, generics.GenericAPIView):
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
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category :
            queryset = Inventory.objects.filter(category = category.lower())

        else :
            queryset = Inventory.objects.all()
        
        return queryset


# to update item fields
class InventoryUpdateAPIView(AdminUserPermissionsMixin, generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def put(self, request):
        try:
            # convert base64_image to raw image

            if(request.data['image']):
                try :
                    image_base64 = request.data.pop('image')
                    image = InvUtils.base64_to_image(image_base64, request.data['image_name'])

                    # update raw data
                    request.data['image'] = image
                except Exception as e :
                    return Response({'status': False, 'message': str(e)}, status = 400)
            # serialize data
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()

            #return response
            return Response({'status': True, 'message' : 'Item Updated Successfully'}, status =200)
           
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status = 400)

# to delete an item from inventory
class InventoryDeleteAPIView(AdminUserPermissionsMixin, generics.DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


#shortnaming
inventory_create_view = InventoryAddItemView.as_view()
inventory_detail_view = InventoryDetailAPIView.as_view()
inventory_list_view =   InventoryListAPIView.as_view()
inventory_update_view = InventoryUpdateAPIView.as_view()
inventory_delete_view = InventoryDeleteAPIView.as_view()
