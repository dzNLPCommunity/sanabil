from django.shortcuts import render
from django.views.generic import ListView

from charity.models import Famille, Necessiteux, AideRecu, Besoin
from staff.models import Association

from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Sum, Count, Q

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
    ordering = ['-id']
    # paginate_by = 10


def age_range(min_age, max_age):
    current = now().date()
    min_date = date(current.year - min_age, current.month, current.day)
    max_date = date(current.year - max_age, current.month, current.day)
    return Count('date_de_naissance', filter=Q(date_de_naissance__gte=max_date) & Q(date_de_naissance__lte=min_date))


class NecessiteuxData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Necessiteux.objects
        qsFamille = Famille.objects.all()
        gender_counts = [0, 0]
        if qs.count() > 0:
            gender_counts[0] = round(qs.filter(sexe='F').count() * 100 / (qs.count()), 2)
            gender_counts[1] = 100 - gender_counts[0]
        gander_data = {
            "labels": ["Femmes", "Hommes"],
            "data": gender_counts,
        }
        enfants = age_range(0, 15)
        ados = age_range(15, 25)
        adults = age_range(25, 65)
        vieux = age_range(65, 150)
        age_counts = [0, 0, 0, 0]
        enfants_count = 0
        labels = ["Enfants", "Adolescents", "Adultes", "Vieux"]
        if qs.count() > 0:
            age_qs = qs.values('date_de_naissance').annotate(enfants=enfants, ados=ados, adults=adults, vieux=vieux)
            age_sums = age_qs.aggregate(enfants_sum=Sum('enfants'), ados_sum=Sum('ados'), adults_sum=Sum('adults'), vieux_sum=Sum('vieux'))
            age_counts = [age_sums['enfants_sum'], age_sums['ados_sum'], age_sums['adults_sum'], age_sums['vieux_sum']]
            enfants_count = age_counts[0]
            unknown_age_count = qs.filter(date_de_naissance__isnull=True).count()
            if unknown_age_count > 0:
                age_counts.append(unknown_age_count)
                labels.append('Âge inconnu')
        age_data = {
            "labels": labels,
            "data": age_counts,
        }
        numbers = {'totale': qs.count(), 'familles': qsFamille.count(),
                   'enfants': enfants_count}
        data = {'gander_data': gander_data, 'age_data': age_data, 'numbers': numbers}
        return Response(data)


class AideRecuListView(ListView):
    model = AideRecu
    #paginate_by = 10


class BesoinListView(ListView):
    model = Besoin
    ordering = ['-nom']

    def get_satisfied_needs(self):
        return self.model.objects.get(est_satisfait=True)

    #paginate_by = 10
