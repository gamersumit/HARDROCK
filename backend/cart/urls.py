from django.urls import path
from . import views 

urlpatterns = [
    path('add/', views.cart_add_view, name='cart-add'),
    path('list/', views.cart_list_view, name='cart-list'),
    path('empty/',views.cart_empty_view , name='cart-empty'),
]
