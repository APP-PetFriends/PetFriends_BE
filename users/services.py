from django.contrib.auth import get_user_model

User = get_user_model()

# 유저 생성
def create_user(*, username: str, email: str, password: str):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    return user
