from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'created_at', 'updated_at')
    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    exclude = ('date_joined', 'username', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
