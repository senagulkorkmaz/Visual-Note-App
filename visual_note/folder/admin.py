from django.contrib import admin
from folder.models import Folder


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id',   'user', 'baslik']
    search_fields = ['id',  'user__first_name', 'user__last_name']
