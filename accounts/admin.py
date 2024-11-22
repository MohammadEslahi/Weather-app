from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (('my fields',{'fields':('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('my fields', {'fields':('age',)}),)


admin.site.register(CustomUser)
admin.site.register(City)