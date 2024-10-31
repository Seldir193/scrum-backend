from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows delete and update permissions only to superusers and staff.
    Authenticated users have read access.
    """
    
    def has_permission(self, request, view):
        """
        Checks permissions based on request type and user role.
        
        Args:
            request: HTTP request.
            view: Accessed view.
        
        Returns:
            bool: Permission status.
        """
        # Restrict delete and update actions to superusers and staff
        if view.action in ['destroy', 'update']:
            return request.user.is_superuser or request.user.is_staff

        # Allow read actions for authenticated users
        return request.user.is_authenticated


