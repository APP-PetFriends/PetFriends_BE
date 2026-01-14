from django.urls import path
from .views import SignupView, LoginView, LogoutView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # 수정
    path('profile-update/', UserUpdateView.as_view(), name='profile-update'),
    
    # 조회
    path('profile/', UserUpdateView.as_view(), name="profile"),
    
    # 삭제
    path('profile-delete/', UserDeleteView.as_view(), name="profile-delete"),
]