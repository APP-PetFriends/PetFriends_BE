# walk/urls.py
from django.urls import path
from .views import WalkRecordView, WalkRecordDetailView

urlpatterns = [
    path('records', WalkRecordView.as_view(), name='walk-record'),
    # <int:pk>는 주소창의 숫자를 pk라는 변수로 view에 넘겨준다는 뜻입니다.
    path('records/<int:pk>/', WalkRecordDetailView.as_view(), name='walk-record-detail'),
]