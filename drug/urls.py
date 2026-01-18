from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrugPlanViewSet, DrugRecordViewSet

router = DefaultRouter()
router.register(r'plans', DrugPlanViewSet)
router.register(r'records', DrugRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
