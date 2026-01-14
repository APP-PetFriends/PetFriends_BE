from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from .serializers import PetCreateSerializer, PetUpdateSerializer

"""
    ModelViewSet이 기본 CRUD를 제공:
    - GET     /pets/       -> list()
    - POST    /pets/       -> create()
    - PATCH   /pets/{id}/  -> partial_update()
    - DELETE  /pets/{id}/  -> destroy()
"""

class PetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # 다른 유저 pet에 접근 못하게 원천 차단
        return Pet.objects.filter(user=self.request.user)
    
    # 이미 serializer에서 user 주입을 해 service를 호출하므로 view에선 안 해도 됨.
    # def create(self, validated_data):
    #     return create_pet(user=self.context["request"].user, **validated_data)

    def get_serializer_class(self):
        if self.action == "create":
            return PetCreateSerializer
        return PetUpdateSerializer
