"""Admin configuration for `core` models."""

from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpRequest
from django.db.models.query import QuerySet

from .models import CustomModel, RelatedItem, User


class RelatedItemInline(admin.TabularInline):
    """Inline admin for `RelatedItem` objects."""

    model = RelatedItem
    extra = 1


@admin.register(CustomModel)
class CustomModelAdmin(admin.ModelAdmin):
    """Admin for `CustomModel` with search, filters and an action."""

    list_display = ('title', 'created', 'description_summary')
    list_filter = ('created',)
    search_fields = ('title', 'description')
    inlines = [RelatedItemInline]
    actions = ['make_title_prefix']

    def description_summary(self, obj: Any) -> str:
        return obj.description[:50]

    description_summary.short_description = 'Description'

    def make_title_prefix(self, request: HttpRequest, queryset: QuerySet) -> None:
        """Prepend 'PREFIX_' to titles of selected objects."""
        for obj in queryset:
            obj.title = f"PREFIX_{obj.title}"
            obj.save()
        self.message_user(request, f"Updated {queryset.count()} items")

    make_title_prefix.short_description = 'Add PREFIX_ to titles'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Extend the default User admin to show `phone_number`."""

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra', {'fields': ('phone_number',)}),
    )
