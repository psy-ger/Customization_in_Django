"""Custom DRF permission classes for the `core` app."""

from typing import Any

from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """Allow safe (read-only) methods for everyone, write methods for staff."""

    def has_permission(self, request: Any, view: Any) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and getattr(request.user, 'is_staff', False))
