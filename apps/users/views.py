from django.contrib.auth.models import update_last_login
from drf_yasg.utils import swagger_auto_schema
from drf_util.decorators import serialize_decorator

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import UserDetailSerializer, GetAllUsersSerializer


User = get_user_model()


class UserRegisterView(GenericAPIView):
    @swagger_auto_schema(request_body=UserDetailSerializer)
    @serialize_decorator(UserDetailSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            is_superuser=True,
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()

        refresh = RefreshToken.for_user(user)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })


class AllUsersListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = GetAllUsersSerializer(users, many=True)
        return Response(serializer.data)
