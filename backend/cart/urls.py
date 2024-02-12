from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('update/', views.cart_update_view, name='cart-update'),
    path('list/', views.cart_list_view, name='cart-list'),
    path('empty/',views.cart_empty_view , name='cart-empty'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
