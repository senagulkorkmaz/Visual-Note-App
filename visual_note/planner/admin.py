from django.contrib import admin
from planner.models import Planner


@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = ['id',   'user', 'baslik']
    search_fields = ['id',  'user__first_name', 'user__last_name']