from django.contrib import admin

from .models import Contact, ContactLabel


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'company', 'position', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'email', 'phone', 'company', 'position', 'memo', 'address')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(ContactLabel)
class ContactLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('id', 'name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
