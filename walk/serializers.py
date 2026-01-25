from rest_framework import serializers
from .models import WalkRecord

class WalkRecordSerializer(serializers.ModelSerializer):

    # 모델의 id를 record_id라는 이름으로 응답에 포함
    record_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = WalkRecord
        #fields = '__all__'  # 혹은 ERD의 모든 필드를 리스트로 나열하세요.
        fields = ['record_id', 'walk_date', 'distance', 'duration', 'weather', 'start_lat', 'start_lon', 'end_lat', 'end_lon']