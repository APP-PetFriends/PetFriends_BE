from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .services import create_user

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    # 생성된 유저 검증
    def create(self, validated_data):
        return create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     # USERNAME_FIELD(email) 기반으로 인증
    #     user = authenticate(**{User.USERNAME_FIELD: data["email"], "password": data["password"]})        
    #     if not user:
    #         raise serializers.ValidationError("이메일 또는 비밀번호가 일치하지 않습니다.")
        
    #     data['user'] = user
    #     return data