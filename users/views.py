from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate

from .serializers import SignupSerializer, LoginSerializer, UserUpdateSerializer



User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "회원 가입이 성공적으로 진행되었습니다."},
            status=status.HTTP_201_CREATED
        )
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # 입력 데이터 -> serializer로 검증
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        if not User.objects.filter(email=email).exists():
            return Response(
                { "message" : "해당 이메일의 계정이 존재하지 않습니다."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        user = authenticate(**{User.USERNAME_FIELD: email, "password": password})
        if not user:
            return Response(
                { "message" : "이메일 또는 비밀번호가 일치하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # JWT 발급
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        return Response(
            {
                "message": "로그인 되었습니다.",
                "user": {"username": user.username, "email": user.email},
                "access": access,
            },
            status=status.HTTP_200_OK
        )
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(
            {"message": "로그아웃 되었습니다. (클라이언트에서 access 토큰을 삭제하세요)"},
            status=status.HTTP_200_OK
        )
        
class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user