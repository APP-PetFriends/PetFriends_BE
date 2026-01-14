from django.contrib import admin
from .models import HealthRecord, HealthSchedule

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ['pet', 'type', 'title', 'date', 'created_at']
    list_filter = ['type', 'date']
    search_fields = ['title', 'note']

@admin.register(HealthSchedule)
class HealthScheduleAdmin(admin.ModelAdmin):
    list_display = ['pet', 'title', 'date', 'location']
    list_filter = ['date']
    search_fields = ['title', 'location', 'note']
