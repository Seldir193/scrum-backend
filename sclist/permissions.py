
# permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Gewährt nur Superusern und Staff-Benutzern das Löschen
        if view.action == 'destroy' or view.action == 'update':
            return request.user.is_superuser or request.user.is_staff
        # Andere Anfragen sind für alle angemeldeten Benutzer erlaubt
        return request.user.is_authenticated
