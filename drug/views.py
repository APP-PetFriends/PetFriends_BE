from django.shortcuts import render
from rest_framework import viewsets
from .models import DrugPlan, DrugRecord
from .serializers import DrugPlanSerializer, DrugRecordSerializer

# Create your views here.
#투약 계획 생성, 조회, 수정, 삭제
class DrugPlanViewSet(viewsets.ModelViewSet):
    queryset = DrugPlan.objects.all()
    serializer_class = DrugPlanSerializer

#투약 기록 생성 담당
class DrugRecordViewSet(viewsets.ModelViewSet):
    queryset = DrugRecord.objects.all()
    serializer_class = DrugRecordSerializer
