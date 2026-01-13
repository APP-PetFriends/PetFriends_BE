from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Pet(models.Model):
    class Gender(models.TextChoices):
        MALE = "M", "수컷"
        FEMALE = "F", "암컷"
        
    class Species(models.TextChoices):
        DOG = "DOG", "강아지"
        CAT = "CAT", "고양이"
        OTHER = "OTHER", "기타"
        
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="pets",
        on_delete=models.CASCADE
    )
    
    # 초기 필수 입력
    name = models.CharField(max_length=50)
    species = models.CharField(
        max_length = 10,
        choices=Species.choices,
    )
    
    # 선택
    breed = models.CharField(max_length=50, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        blank=True,
    )
    birth = models.DateField(blank=True, null=True)
    
    pet_image = models.ImageField(upload_to="pets/", blank=True, null=True)
    weight = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.1)]
    )    
    is_neutered = models.BooleanField(default=False)
    allergy = models.JSONField(blank=True, null=True)
    etc = models.TextField(blank=True, null=True)
    
    # 다른 유저 간의 동일한 pet.name은 괜찮지만, 같은 유저 간의 중복 pet.name은 불가
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                
                # DB 제약 조건 이름!
                name="unique_pet_name_per_user",
            )
        ]
        
    # 객체를 문자열로 보여줄 때 사용
    def __str__(self):
        return f"{self.user_id}-{self.name}"