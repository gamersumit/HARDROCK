from django.urls import path
from . import views 

urlpatterns = [
    path('add/', views.cart_add_view, name='cart-add'),
    # path('cart/items/', CartItemListCreate.as_view(), name='cart-item-list-create'),
    # path('cart/items/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),
]
