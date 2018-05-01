from django.shortcuts import render
from dynamic_rest.viewsets import DynamicModelViewSet

from staff.models import  Membre, Login, User, Role
from staff.serializers import  AgentSerializer, LoginSerializer, UserSerializer, \
    RoleSerializer


class AgentViewSet(DynamicModelViewSet):
    queryset = Membre.objects.all()
    serializer_class = AgentSerializer

class LoginViewSet(DynamicModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class UserViewSet(DynamicModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(DynamicModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
