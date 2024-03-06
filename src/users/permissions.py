from rest_framework.permissions import BasePermission


class IsCartOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer


class IsCartItemOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.cart.customer
