from django.db import IntegrityError
from .models import Pet

class DuplicatePetNameError(Exception):
    pass

def create_pet(*, user, **pet_data) -> Pet:
    try:
        return Pet.objects.create(user=user, **pet_data)
    except IntegrityError:
        # (user, name) Unique 제약 위반 시
        raise DuplicatePetNameError("이미 등록된 반려동물 이름입니다.")