from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthRecordViewSet, HealthScheduleViewSet

router = DefaultRouter()
router.register(r'records', HealthRecordViewSet)
router.register(r'schedules', HealthScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),  # ← api/health/ 삭제!
]
