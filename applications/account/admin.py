from django.contrib import admin
from applications.account.models import CustomUser, Group
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_filter = ()


# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Group)
