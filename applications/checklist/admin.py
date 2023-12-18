from django.contrib import admin
from applications.checklist.models import Toast


class ToastAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'shift', 'datetime')


# Register your models here.
admin.site.register(Toast, ToastAdmin)
