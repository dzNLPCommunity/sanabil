from django.contrib.auth.models import Group, Permission
from dynamic_rest.serializers import DynamicModelSerializer

from base.models import  Wilaya, Commune, Parameter



class WilayaSerializer(DynamicModelSerializer):
    class Meta:
        model = Wilaya
        fields = '__all__'



class CommuneSerializer(DynamicModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'


class ParameterSerializer(DynamicModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'


class GroupSerializer(DynamicModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(DynamicModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'