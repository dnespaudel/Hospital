from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class isAdmin(BasePermission):
    message = "Viewing&Editing fields is restricted to specified roles only!"

    def has_permission(self, request, view):
        if request.user.role == 'A':
            return True
        return False


class isManager(BasePermission):
    message = "Viewing&Editing fields is restricted to specified roles only!"

    def has_permission(self, request, view):
        if request.user.role == 'M':
            return True
        return False


class isPatient(BasePermission):
    message = "Viewing&Editing fields is restricted to specified roles only!"

    def has_permission(self, request, view):
        if request.user.role == 'P' and request.method in permissions.SAFE_METHODS:
            return True
        return False


class isDoctor(BasePermission):
    message = "Viewing&Editing fields is restricted to specified roles only!"

    def has_permission(self, request, view):
        if request.user.role == 'D':
            return True
        return False


class isNurse(BasePermission):
    message = "Viewing&Editing fields is restricted to specified roles only!"

    def has_permission(self, request, view):
        if request.user.role == 'N':
            return True
        return False


class isReceptionist(BasePermission):
    message = "Viewing&Editing fields is restricted to specified roles only!"

    def has_permission(self, request, view):
        if request.user.role == 'R':
            return True
        return False


class isAdminOrReadOnly(BasePermission):
    message = "Not Allowed !"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "PUT" and request.user.is_anonymous:
            return False
        if request.method == "PUT" and request.user.role == "A":
            return True
        if request.method == "DELETE" and request.user.is_anonymous:
            return False
        if request.method == "DELETE" and request.user.role == "A":
            return True


