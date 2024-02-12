from django.shortcuts import render
from rest_framework import generics
from account.mixins import CustomerUserPermissionsMixin
from inventory.models import Inventory
from account.models import CustomUser
from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import AccessToken

class CartUpdateView(CustomerUserPermissionsMixin, generics.GenericAPIView) :
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    
    def post(self, request) :
        try :
            # fetch user from request
                token = request.headers.get('Authorization').split()[1]
                user = AccessToken(token).payload.get('user_id')
                
                # fectch product which user wants to add to the cart
                product = request.data.get('product')
               
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
    
class CartEmptyCartView(CustomerUserPermissionsMixin, generics.GenericAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    
    def delete(self, request):
        try:
            # fetch user from request
            token = request.headers.get('Authorization').split()[1]
            user = AccessToken(token).payload.get('user_id')
            
            # empty cart/ delte items from cart where user = request.user
            Cart.objects.filter(user=user).delete()
            return Response({'status': True, "message" : "cart items deleted successfully"}, status = 200)
         
        except Exception as e:
             return Response({'status': False, "message" : str(e)}, status = 400)


# #shortnaming
cart_update_view = CartUpdateView.as_view()
cart_list_view =  CartListAPIView.as_view()
cart_empty_view = CartEmptyCartView.as_view()
