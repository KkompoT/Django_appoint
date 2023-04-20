from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Если метод безопасный, даем доступ всем пользователям
            return True

        return bool(request.user and request.user.is_staff)  # А иначе, только для администратора

class IsOwnerOrReadOnly(permissions.BasePermission):  # Права на уровне одной записи, для тех позователей кто создал запись
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user