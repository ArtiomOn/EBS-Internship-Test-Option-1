from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import UserRegisterView, AllUsersListView

urlpatterns = [
    path('user/list/', AllUsersListView.as_view(), name='users_list'),
    path('user/register/', UserRegisterView.as_view(), name='user_register'),
    path('user/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
