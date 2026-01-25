from django.db import models

# Create your models here.

#1. 투약 계획
class DrugPlan(models.Model):
    pet_name = models.CharField(max_length=50, verbose_name="반려동물 이름")
    drug_name = models.CharField(max_length=100, verbose_name="약 이름")    #약 이름
    dosage = models.CharField(max_length=50, verbose_name="용량/단위")

    FREQUENCY_CHOICES = [
        ('DAILY', '매일'),
        ('EOD', '격일'),
        ('WEEKLY', '주 N회'), 
        ('CUSTOM', '사용자 지정')
    ]
    frequency = models.CharField(
        max_length=20, 
        choices=FREQUENCY_CHOICES,
        default='DAILY', 
        verbose_name="복용 주기"
    )

    start_date = models.DateField(verbose_name="시작일") #복용 시작일
    end_date = models.DateField(null=True, blank=True, verbose_name="종료일")  #복용 종료일
    
    is_active = models.BooleanField(default=True, verbose_name="활성 계획")   #활성 여부
    memo = models.TextField(null=True, blank=True, verbose_name="메모")  #메모

    def __str__(self):
        return f"{self.drug_name} ({self.pet_name})"

#2. 투약 시각 (복수 설정 가능)
class DrugTime(models.Model):
    plan = models.ForeignKey(DrugPlan, related_name='times', on_delete=models.CASCADE)  #주기 아이디
    time_of_day = models.TimeField(verbose_name="복용 시간")    #복용 시각
    seq = models.IntegerField(default=1, verbose_name="복용 순번") #복용 순번

#3. 투약 기록
class DrugRecord(models.Model):
    plan = models.ForeignKey(DrugPlan, on_delete=models.CASCADE, related_name='records')    #계획 아이디
    schedule_at = models.DateTimeField(verbose_name="예정 일시")   #예정 일시
    is_taken = models.BooleanField(default=False, verbose_name="복용 여부")
    taken_at = models.DateTimeField(null=True, blank=True, verbose_name="실제 복용 시각")  #실제 복용 시각