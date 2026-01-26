from rest_framework import serializers
from .models import HealthRecord, HealthSchedule

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class HealthScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthSchedule
        fields = '__all__'
