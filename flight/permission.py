from itertools import permutations
from rest_framework import permissions

class IsStaffPermission(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.auth:
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return request.user.is_staff
        else:
            return False