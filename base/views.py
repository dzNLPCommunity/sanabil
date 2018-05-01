from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token as Rest_Token
from rest_framework.response import Response

from base.models import  Wilaya, Commune, Gender, Parameter, PhoneType, AgeCategory
from base.serializers import  WilayaSerializer, CommuneSerializer, GenderSerializer, ParameterSerializer, \
    PhoneTypeSerializer, GroupSerializer, PermissionSerializer, AgeCategorySerializer


def index(request):
    t = get_template('index.html')
    html = t.render({})
    return HttpResponse(html)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Rest_Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})



class WilayaViewSet(DynamicModelViewSet):
    queryset = Wilaya.objects.all()
    serializer_class = WilayaSerializer


class CommuneViewSet(DynamicModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer


class GenderViewSet(DynamicModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class ParameterViewSet(DynamicModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class PhoneTypeViewSet(DynamicModelViewSet):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeSerializer


class GroupViewSet(DynamicModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(DynamicModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class AgeCategoryViewSet(DynamicModelViewSet):
    queryset = AgeCategory.objects.all()
    serializer_class = AgeCategorySerializer


