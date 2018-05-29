from django.shortcuts import render
from dynamic_rest.viewsets import DynamicModelViewSet

from staff.models import  Membre, Login
from staff.serializers import  AgentSerializer, LoginSerializer


class AgentViewSet(DynamicModelViewSet):
    queryset = Membre.objects.all()
    serializer_class = AgentSerializer

class LoginViewSet(DynamicModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

