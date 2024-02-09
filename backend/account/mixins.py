from rest_framework import permissions
from .permissions import AdminUserPermissions  

class AdminUserPermissionsMixin(AdminUserPermissions) :
    permission_classes = [
       permissions.IsAuthenticated, 
       AdminUserPermissions
    ]