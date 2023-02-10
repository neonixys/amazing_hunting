from django.urls import path
from rest_framework.authtoken import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateView, Logout

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]