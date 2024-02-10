from django.urls import path
from . import views 

urlpatterns = [
    path('add/', views.cart_add_view, name='cart-add'),
    path('list/', views.cart_list_view, name='cart-list'),
    # path('cart/items/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),
]
