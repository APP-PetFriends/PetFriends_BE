from django.db import models
from pet.models import Pet

class HealthRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('vaccination', '접종'),
        ('disease', '지병'),
    ]
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='health_records')
    type = models.CharField(max_length=20, choices=RECORD_TYPE_CHOICES)
    title = models.CharField(max_length=100)
    date = models.DateField()
    note = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.pet.name} - {self.get_type_display()} - {self.title}"

class HealthSchedule(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='health_schedules')
    title = models.CharField(max_length=100)  # 병원, 미용 등
    date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"{self.pet.name} - {self.title} - {self.date}"
