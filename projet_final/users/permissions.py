from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.http import HttpResponse
from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission

from .models import User

STAFF_ROLES = {User.Role.ADMIN, User.Role.EMPLOYE}


def has_staff_role(user: User) -> bool:
    """Return whether a user may manage the business back office."""
    return user.is_superuser or user.role in STAFF_ROLES


def has_admin_role(user: User) -> bool:
    """Return whether a user has the administrator business role."""
    return user.is_superuser or user.role == User.Role.ADMIN


def staff_role_required(
    view_func: Callable[..., HttpResponse],
) -> Callable[..., HttpResponse]:
    """Require a logged-in administrator or employee for a view."""

    @wraps(view_func)
    def wrapped(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not has_staff_role(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapped


def admin_role_required(
    view_func: Callable[..., HttpResponse],
) -> Callable[..., HttpResponse]:
    """Require a logged-in administrator for a view."""

    @wraps(view_func)
    def wrapped(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not has_admin_role(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapped


class StaffRoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Class-based-view equivalent of :func:`staff_role_required`."""

    def test_func(self) -> bool:
        return has_staff_role(self.request.user)


class AdminRoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Class-based-view access for administrators only."""

    def test_func(self) -> bool:
        return has_admin_role(self.request.user)


class IsBusinessStaff(BasePermission):
    """Allow API management only to an administrator or an employee."""

    message = "Cette action est réservée aux employés et administrateurs."

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return request.user.is_authenticated and has_staff_role(request.user)


class IsBusinessAdmin(BasePermission):
    """Allow API access only to an administrator."""

    message = "Cette action est réservée aux administrateurs."

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return request.user.is_authenticated and has_admin_role(request.user)


class CanManageArticles(BasePermission):
    """Employees can read/create articles; only admins can alter or delete them."""

    message = "Seul un administrateur peut modifier ou supprimer un article."

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        if not request.user.is_authenticated or not has_staff_role(request.user):
            return False
        return has_admin_role(request.user) or request.method in {*SAFE_METHODS, "POST"}
