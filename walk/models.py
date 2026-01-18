from django.db import models

# Create your models here.


#class Pet(models.Model):
    # 기존에 작성된 반려동물 모델
   # name = models.CharField(max_length=100)
    # ... 기타 필드

class WalkRecord(models.Model):
    # record_id는 Django가 자동으로 생성하는 pk를 사용하거나 명시합니다.
    pet = models.ForeignKey('pet.Pet', on_delete=models.CASCADE, related_name='walk_records')
    walk_date = models.DateField(verbose_name="산책 날짜")
    start_lat = models.FloatField(verbose_name="시작 위도")
    start_lon = models.FloatField(verbose_name="시작 경도")
    end_lat = models.FloatField(verbose_name="종료 위도")
    end_lon = models.FloatField(verbose_name="종료 경도")
    duration = models.IntegerField(verbose_name="산책 시간(분)")
    distance = models.FloatField(verbose_name="산책 거리(km)")
    weather = models.CharField(max_length=50, null=True, blank=True, verbose_name="날씨 정보")

    def __str__(self):
        return f"{self.pet.name} - {self.walk_date}"