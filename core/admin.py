from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Feedback

# Custom UserAdmin to show 'role' and 'manager' in admin
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role", "manager")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "role", "manager")
    list_filter = ("role",)

admin.site.register(User, UserAdmin)
admin.site.register(Feedback)
