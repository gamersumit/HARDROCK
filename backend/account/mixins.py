from rest_framework import permissions
from .permissions import AdminUserPermissions, CustomerUserPermissions 

class AdminUserPermissionsMixin(AdminUserPermissions) :
    permission_classes = [
       permissions.IsAuthenticated, 
       AdminUserPermissions,
    ]

class CustomerUserPermissionsMixin(CustomerUserPermissions) :
    permission_classes = [
       permissions.IsAuthenticated, 
       CustomerUserPermissions,
    ]