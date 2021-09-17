from rest_framework import permissions


class IsAdminOrViewOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser and request.method != 'POST':
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser and request.method == 'GET':
            return True
