from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'followers')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
