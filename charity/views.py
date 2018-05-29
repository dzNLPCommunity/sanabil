from django.shortcuts import render

# Create your views here.
from dynamic_rest.viewsets import DynamicModelViewSet

from charity.models import Association, Famille, Necessiteux, Centre, Besoin, Donneur, AideRecu
from charity.serializers import AssociationSerializer, FamilleSerializer, NecessiteuxSerializer, CentreSerializer, \
    BesoinSerializer, DonneurSerializer, AideRecuSerializer


class AssociationViewSet(DynamicModelViewSet):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer


class FamilleViewSet(DynamicModelViewSet):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer


class NecessiteuxViewSet(DynamicModelViewSet):
    queryset = Necessiteux.objects.all()
    serializer_class = NecessiteuxSerializer



class CentreViewSet(DynamicModelViewSet):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer


class BesoinViewSet(DynamicModelViewSet):
    queryset = Besoin.objects.all()
    serializer_class = BesoinSerializer



class DonneurViewSet(DynamicModelViewSet):
    queryset = Donneur.objects.all()
    serializer_class = DonneurSerializer


class AideRecuViewSet(DynamicModelViewSet):
    queryset = AideRecu.objects.all()
    serializer_class = AideRecuSerializer



