from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if isinstance(data, dict) and data.get('password'):
            data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        if isinstance(data, dict) and data.get('password'):
            data['password'] = make_password(data['password'])
        return self.guardar(data, partial=False)

    def partial_update(self, request, *args, **kwargs):
        data = request.data.copy()
        password = data.get('password') if isinstance(data, dict) else None
        if password:
            data['password'] = make_password(password)
        elif isinstance(data, dict) and 'password' in data:
            data['password'] = self.get_object().password
        return self.guardar(data, partial=True)

    def guardar(self, data, partial):
        serializer = self.get_serializer(self.get_object(), data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class getPerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
