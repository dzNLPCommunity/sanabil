from django.views.generic import ListView

from staff.models import Association


class AssociationListView(ListView):
    model = Association
    paginate_by = 10