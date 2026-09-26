from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, **kwargs):
        if not kwargs.get('partial') and 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data.get('password')
        if password:
            request.data['password'] = make_password(password)
        elif 'password' in request.data:
            request.data['password'] = self.get_object().password
        return super().partial_update(request, *args, **kwargs)

class getPerfilView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)