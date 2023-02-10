from rest_framework.permissions import BasePermission

from authentication.models import User


class VacancyCreatePermission(BasePermission):
    message = "Adding vacancy for non hr users not allowed"

    def has_permission(self, request, view):
        if request.user.role == User.HR:
            return True
        return False
