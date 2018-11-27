from django.views.generic import ListView

from staff.models import Association


class AssociationListView(ListView):
    model = Association
    ordering = ['-nom']
    paginate_by = 10