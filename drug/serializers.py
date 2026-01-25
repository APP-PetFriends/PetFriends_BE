from rest_framework import serializers
from .models import DrugPlan, DrugTime, DrugRecord

# #1. 투약 시각
class DrugTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugTime
        fields = ['time_of_day']

# #2. 투약 계획 (메인)
class DrugPlanSerializer(serializers.ModelSerializer):
    times = DrugTimeSerializer(many=True) 

    class Meta:
        model = DrugPlan
        fields = [
            'id', 'pet_name', 'drug_name', 'dosage', 
            'frequency', 'times', 'start_date', 'end_date', 
            'memo', 'is_active' 
        ]

    def create(self, validated_data):
        times_data = validated_data.pop('times')
        plan = DrugPlan.objects.create(**validated_data)
        for i, time_data in enumerate(times_data):
            DrugTime.objects.create(plan=plan, seq=i+1, **time_data)
        return plan

# #3. 투약 기록 
class DrugRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugRecord
        fields = '__all__'