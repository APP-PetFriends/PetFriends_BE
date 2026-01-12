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