from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('<int:pk>/', views.inventory_detail_view, name = 'getitem'), 
    path('add/', views.inventory_create_view, name = 'add_item'),
    path('list/<str:category>/', views.inventory_list_view, name = 'category_items'),
    path('list/', views.inventory_list_view, name = 'all_items'),
    path('<int:pk>/update/', views.inventory_update_view, name = 'update_item'),
    path('<int:pk>/delete/', views.inventory_delete_view, name = 'delete_item'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)