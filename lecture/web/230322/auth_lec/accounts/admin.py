from django.contrib import admin
# UserAdmin: User 데이터를 입력받는 Form
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "nickname", )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "nickname",),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
# Register your models here.
admin.site.register(User, CustomUserAdmin)
