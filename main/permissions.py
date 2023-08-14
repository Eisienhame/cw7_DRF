from rest_framework import permissions
from rest_framework.permissions import BasePermission


class HabitPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False

