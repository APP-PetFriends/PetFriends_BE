from rest_framework import serializers
from .models import Pet
from .services import create_pet, DuplicatePetNameError

class PetCreateSerializer(serializers.ModelSerializer):
    # user는 응답에는 보이되, 요청에서는 못 보내게(서버에서 주입)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = ("id","user","name", "species", "breed", "gender", "birth", "pet_image",)
        
        '''
        DRF 필수값 검증에 맡김
        def validate(self, data):
            if not data.get("name"):
                raise serializers.ValidationError("이름은 필수 입력값입니다.")
            if not data.get("species"):
                raise serializers.ValidationError("종은 필수 선택값입니다.")
            return data
        '''
        
    def create(self, validated_data):
        """
        validated_data는 DRF가 검증해준 데이터.
        request.user는 ViewSet이 serializer context에 자동으로 넣어줌.
        """
        user = self.context["request"].user
        try:
            return create_pet(user=user, **validated_data)
        except DuplicatePetNameError as e:
            raise serializers.ValidationError({"name":str(e)})
        
class PetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("id", "name", "species", "breed", "gender", "birth", "pet_image", "weight", "is_neutered", "allergy", "etc")