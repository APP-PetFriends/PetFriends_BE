from django.urls import path
from .views import SignupView, LoginView, LogoutView, UserUpdateView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserUpdateView.as_view(), name='user-me'),
    path('profile/', UserUpdateView.as_view(), name="user-profile"),
]