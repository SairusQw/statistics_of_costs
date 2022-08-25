from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from costs.forms import CustomUserCreationForm, CustomUserChangeForm
from costs.models import Cost, CustomUser

admin.site.register(Cost)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)
