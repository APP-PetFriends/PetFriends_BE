from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .services import create_user

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, data):
        pw1 = data.get("password")
        pw2 = data.get("password2")
        if pw1 != pw2:
            raise serializers.ValidationError("입력한 비밀번호가 일치하지 않습니다.")
        validate_password(pw1)
        return data
        
    # 생성된 유저 검증
    def create(self, validated_data):
        validated_data.pop("password2")
        return create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
        return value
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
        read_only_fields = ("email", "username")
