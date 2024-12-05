from django.urls import path
from .views import MyUserAPI, TestTokenAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("", MyUserAPI),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("testtoken", TestTokenAPI, name = 'test_token'),
    path("<str:id>", MyUserAPI),
    
]