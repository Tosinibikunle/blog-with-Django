from django.contrib import admin
from .models import CustomBlogger, customReader



@admin.register(CustomBlogger)
class CustomBloggerAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_verified', 'is_staff', 'created_at')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_verified', 'is_staff', 'is_superuser', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'bio', 'profile_picture')}),
        ('Permissions', {'fields': ('is_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'last_login_ip', 'created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(customReader)
class CustomReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_genres', 'subscribed_newsletter', 'created_at')
    search_fields = ('user__email', 'user__username', 'favorite_genres')
    list_filter = ('subscribed_newsletter', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Preferences', {'fields': ('favorite_genres', 'subscribed_newsletter')}),
        ('Important Dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')    