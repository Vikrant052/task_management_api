from django.contrib import admin
from .models import User  # Import your custom User model

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'email')  # Show these fields in the list view
    search_fields = ('username', 'mobile', 'email')  # Searchable fields
    ordering = ('username',)  # Sort by username
    fields = ('username', 'mobile', 'email')  # Fields to display when editing
    list_filter = ()  # Remove filters like 'is_staff'

admin.site.register(User, CustomUserAdmin)
