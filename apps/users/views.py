from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, GetUserSerializer
from drf_util.decorators import serialize_decorator
from rest_framework.views import APIView
# Create your views here.


class RegisterUserView(GenericAPIView):
    @swagger_auto_schema(request_body=UserSerializer)
    @serialize_decorator(UserSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            is_superuser=True,
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()

        return Response(UserSerializer(user).data)


class GetListUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data)


