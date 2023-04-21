from rest_framework import permissions

"""Класс определяет пользовательские разрешения ,
 который предоставляет доступ только для чтения любому пользователю,
  и ограничивает доступ для записи, кроме администратора """


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Если метод безопасный, даем доступ всем пользователям
            return True

        return bool(request.user and request.user.is_staff)  # А иначе, только для администратора


"""Класс определяет пользовательские разрешения ,
который, разрешает доступ на запись только тому кто создал запись в базе,
 на чтение любому пользователю"""


class IsOwnerOrReadOnly(
    permissions.BasePermission):  # Права на уровне одной записи, для тех позователей кто создал запись
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
