from django.contrib import admin
from diary.models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['id',   'user', 'baslik']
    search_fields = ['id',  'user__first_name', 'user__last_name']