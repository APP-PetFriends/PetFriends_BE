from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from .models import HealthRecord, HealthSchedule
from .serializers import HealthRecordSerializer, HealthScheduleSerializer

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
    
    def get_queryset(self):
        pet_id = self.request.query_params.get('pet_id')
        if pet_id:
            return self.queryset.filter(pet_id=pet_id)
        return self.queryset
    
    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            return Response(
                {'error': '이미 존재하는 기록입니다.'}, 
                status=status.HTTP_409_CONFLICT
            )

class HealthScheduleViewSet(viewsets.ModelViewSet):
    queryset = HealthSchedule.objects.all()
    serializer_class = HealthScheduleSerializer
    
    def get_queryset(self):
        pet_id = self.request.query_params.get('pet_id')
        if pet_id:
            return self.queryset.filter(pet_id=pet_id)
        return self.queryset
