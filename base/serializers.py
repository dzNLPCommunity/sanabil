from django.contrib.auth.models import Group, Permission
from dynamic_rest.serializers import DynamicModelSerializer

from base.models import  Wilaya, Commune, Parameter, CentreType, DonType, DonneurType, NiveauScolaire, \
    SituationFamiliale, SituationProfessionelle


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


class CentreTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = CentreType
        fields = '__all__'



class DonTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = DonType
        fields = '__all__'


class DonneurTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = DonneurType
        fields = '__all__'


class NiveauScolaireSerializer(DynamicModelSerializer):
    class Meta:
        model = NiveauScolaire
        fields = '__all__'



class SituationFamilialeSerializer(DynamicModelSerializer):
    class Meta:
        model = SituationFamiliale
        fields = '__all__'


class SituationProfessionelleSerializer(DynamicModelSerializer):
    class Meta:
        model = SituationProfessionelle
        fields = '__all__'
