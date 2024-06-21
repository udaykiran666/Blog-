from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to create and update categories.
    """

    def has_permission(self, request, view):
        # Allow all users to list or retrieve
        if view.action in ['list', 'retrieve']:
            return True
        # Only superusers can create or update
        return request.user and request.user.is_superuser
