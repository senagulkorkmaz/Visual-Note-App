from django.contrib import admin
from note.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id',   'user', 'baslik']
    search_fields = ['id',  'user__first_name', 'user__last_name']
