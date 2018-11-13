from django.shortcuts import render
from django.views.generic import ListView

from charity.models import Famille, Necessiteux, AideRecu, Besoin
from staff.models import Association

from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count, Q

from datetime import date
from django.utils.timezone import now


def homepage(request):
    return render(request,
                  'home.html',
                  {"stat": {
                      'familles': Famille.objects.count(),
                      'necessiteux': Necessiteux.objects.count(),
                      'aides': AideRecu.objects.count(),
                      'association': Association.objects.count()
                  }}
                  )


def helppage(request):
    return render(request,
                  'help.html',
                  {}
                  )


class NecessiteuxListView(ListView):
    model = Necessiteux
    paginate_by = 10


def age_range(min_age, max_age):
    current = now().date()
    min_date = date(current.year - min_age, current.month, current.day)
    max_date = date(current.year - max_age, current.month, current.day)
    return Count('date_de_naissance', filter=Q(date_de_naissance__gte=max_date) & Q(date_de_naissance__lte=min_date))


class NecessiteuxData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Necessiteux.objects.all()
        qsFamille = Famille.objects.all()
        gender_qs = qs.annotate(count=Count('sexe'))
        gender_counts = [0, 0]
        for person in gender_qs:
            if person.sexe == 'F':
                gender_counts[0] = person.count
            else:
                gender_counts[1] = person.count
        gender_counts[0] = round(gender_counts[0] * 100 / (gender_counts[0]+gender_counts[1]), 2)
        gender_counts[1] = 100 - gender_counts[0]
        gander_data = {
            "labels": ["Femmes", "Hommes"],
            "data": gender_counts,
        }
        enfants = age_range(0, 18)
        jeunes = age_range(19, 25)
        adults = age_range(26, 59)
        vieux = age_range(60, 150)
        age_counts = [0, 0, 0, 0, 0]
        enfants_count = 0
        if qs.count() > 0:
            age_qs = qs.annotate(enfants=enfants).annotate(jeunes=jeunes).annotate(adults=adults).annotate(vieux=vieux)
            age_counts = [age_qs[0].enfants, age_qs[0].jeunes, age_qs[0].adults, age_qs[0].vieux]
            enfants_count = age_qs[0].enfants
        age_data = {
            "labels": ["Enfants", "Jeunes", "Adultes", "Vieux"],
            "data": age_counts,
        }
        numbers = {'totale': qs.count(), 'familles': qsFamille.count(),
                   'enfants': enfants_count}
        data = {'gander_data': gander_data, 'age_data': age_data, 'numbers': numbers}
        return Response(data)


class AideRecuListView(ListView):
    model = AideRecu
    paginate_by = 10


class BesoinListView(ListView):
    model = Besoin

    def get_satisfied_needs(self):
        return self.model.objects.get(est_satisfait=True)

    paginate_by = 10
