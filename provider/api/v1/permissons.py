from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        return request.method in self.SAFE_METHODS
