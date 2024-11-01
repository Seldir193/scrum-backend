from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission class that allows only admin, staff, and guest users to delete or update tasks.
    Normal users can only create or read tasks.
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
        # Allow only superusers, staff, and guest users to delete or update tasks
        if view.action in ['destroy', 'update']:
            return request.user.is_superuser or request.user.is_staff or request.user.username == "guest"
        
        # Other actions (create, read) are allowed for all authenticated users
        return request.user.is_authenticated
