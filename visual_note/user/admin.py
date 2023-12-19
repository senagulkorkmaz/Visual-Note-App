from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id',   'first_name', 'last_name', 'email']
    search_fields = ['id',  'first_name', 'last_name', 'email']
