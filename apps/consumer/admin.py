from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from django.contrib import admin
from apps.consumer.models import User
# Register your models here.
ser = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name", "first_name", "dni", "direction", "phone", "types_user", "gender", "is_student", "is_teacher", "is_moderator")}),
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
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ["email", "name", "is_superuser"]
    ordering = ['email']
    search_fields = ["name"]
