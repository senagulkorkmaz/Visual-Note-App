from django.contrib import admin
from to_do_list.models import To_Do_List


@admin.register(To_Do_List)
class To_Do_ListAdmin(admin.ModelAdmin):
    list_display = ['id',   'user', 'baslik']
    search_fields = ['id',  'user__first_name', 'user__last_name']
