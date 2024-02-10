from django.shortcuts import render
from rest_framework import generics
from account.mixins import AdminUserPermissionsMixin
from inventory.models import Inventory
from account.models import CustomUser
from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view




class CartAddItemView(generics.GenericAPIView) :
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    
    def post(self, request) :
        try :
            # fetch user from request
                token = request.headers.get('Authorization').split()[1]
                user = AccessToken(token).payload.get('user_id')
                # user = CustomUser.objects.get(id = user)

                # fectch product which user wants to add to the cart
                product = request.data.get('product')
                # product = Inventory.objects.get(id = product)
            
                # fectch quantity if item
                quantity = request.data.get('quantity', 1)

                # data to serialize
                data = {'user' : user, "product" : product, "quantity" : quantity}

                serializer = self.serializer_class(data = data)
                serializer.is_valid(raise_exception = True)

                # if item already exist
                if Cart.objects.filter(user = user, product = product).exists() :
                    cart_item = Cart.objects.get(user = user, product = product)
                    cart_item.quantity += quantity

                    # stock availblity : 
                    product = Inventory.objects.get(id = product)        
                    if cart_item.quantity > product.quantity :
                         return Response({"status": False, "message" : "Quantity added in the cart is more than the stock", "stock" : product.quantity}, status = 400)
                   
                    cart_item.save()

                    if cart_item.quantity < 0 :
                         cart_item.delete()
                
                else :
                    serializer.save()
                
                return Response({'status': True, 'message' : 'Item added Successfully'}, status =200)

        except Exception as e:
                return Response({'status': False, 'message' : str(e)}, status = 400)

      
class CartListAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_class = [permissions.IsAuthenticated]
   
    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        user = AccessToken(token).payload.get('user_id')
        return Cart.objects.filter(user=user)
    
    # def get(self, request):
    #       # fetch user from request
    #     try :
    #         token = request.headers.get('Authorization').split()[1]
    #         user = AccessToken(token).payload.get('user_id')
    #         queryset = Cart.objects.filter(user = user)
    #         # product = [Inventory.objects.get(id = item.product) for item in queryset]
    #         return Response({"status" : True, "data" : list(queryset)}, status = 200)
    #     except Exception as e:
    #         return Response({"status" : False, "message" : str(e)}, status = 400)
# class InventoryUpdateAPIView(generics.UpdateAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer

# class InventoryDeleteAPIView(generics.DestroyAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer


# #shortnaming
cart_add_view = CartAddItemView.as_view()
# inventory_detail_view = InventoryDetailAPIView.as_view()
cart_list_view =   CartListAPIView.as_view()
# inventory_update_view = InventoryUpdateAPIView.as_view()
# inventory_delete_view = InventoryDeleteAPIView.as_view()
