from rest_framework import permissions


class IsAdminOrViewOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method not in ['POST', ]:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == 'GET':
            return True
