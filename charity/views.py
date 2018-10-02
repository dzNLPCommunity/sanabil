from django.shortcuts import render
from django.views.generic import ListView

from charity.models import Famille, Necessiteux, AideRecu, Besoin
from staff.models import Association


def homepage(request):
    return render(request,
                  'home.html',
                  {"stat":{
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


class AideRecuListView(ListView):
    model = AideRecu
    paginate_by = 10

class BesoinListView(ListView):
    model = Besoin
    paginate_by = 10