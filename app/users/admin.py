from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model

from .models import BusinessUnit, Department, Team

User = get_user_model()


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = (
        "username",
        "name",
        "team",
        "email",
        "last_login",
        "is_superuser",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Information", {"fields": ("name", "email")}),
        ("Role Information", {"fields": ("team",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ("name", "email")
