from dynamic_rest.serializers import DynamicModelSerializer

from charity.models import Association, Famille, Necessiteux, Centre, Besoin, Donneur, AideRecu
from staff.models import  Membre, Login

class AssociationSerializer(DynamicModelSerializer):
    class Meta:
        model = Association
        fields = '__all__'



class FamilleSerializer(DynamicModelSerializer):
    class Meta:
        model = Famille
        fields = '__all__'


class NecessiteuxSerializer(DynamicModelSerializer):
    class Meta:
        model = Necessiteux
        fields = '__all__'


class CentreSerializer(DynamicModelSerializer):
    class Meta:
        model = Centre
        fields = '__all__'


class BesoinSerializer(DynamicModelSerializer):
    class Meta:
        model = Besoin
        fields = '__all__'


class DonneurSerializer(DynamicModelSerializer):
    class Meta:
        model = Donneur
        fields = '__all__'


class AideRecuSerializer(DynamicModelSerializer):
    class Meta:
        model = AideRecu
        fields = '__all__'
