from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

# Desregistras el UserAdmin predeterminado
admin.site.unregister(User)
# Registras tu UserAdmin personalizado
admin.site.register(User, UserAdmin)