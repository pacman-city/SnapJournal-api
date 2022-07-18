from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        """Fn -> True, if: safe-method | authorized"""
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Fn -> True, if: safe-method | is_post_owner"""
        return (request.method in SAFE_METHODS
                or obj.author == request.user)
