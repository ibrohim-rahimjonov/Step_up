from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms import ModelForm
from .models import User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'role', 'address', 'password']


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'full_name', 'username', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email', 'full_name', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'address', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'address', 'role', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
