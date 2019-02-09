from django.apps import apps
from django.contrib import admin

from charity.models import Association, Famille, Necessiteux, Centre, Besoin, Donneur, AideRecu


@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):
    list_display = ["nom", "nombre_enfant"]
    list_display_links = ["nom"]
    search_fields = ["nom"]
    list_filter = ["nombre_enfant"]


@admin.register(Necessiteux)
class NecessiteuxAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "tel", "association"]
    list_display_links = ["nom", "prenom"]
    search_fields = ["nom", "prenom", "tel"]
    list_filter = ['sexe', 'niveau_scolaire', 'pointure', 'taille', 'situation_familiale', 'situation_professionelle',
                   'est_orphelin', 'represent_famille', 'degré_nécessite', 'archivé', 'est_permanent']
    radio_fields = {'sexe': admin.HORIZONTAL, 'degré_nécessite': admin.HORIZONTAL}


@admin.register(Centre)
class CentreAdmin(admin.ModelAdmin):
    list_display = ["nom", "address"]
    list_display_links = ["nom"]
    search_fields = ["nom", "address"]
    list_filter = ["type"]


def satisfy_need(modeladmin, request, queryset):
    for need in queryset:
        need.est_satisfait = True
        need.save()


satisfy_need.short_description = 'Satisfaire les besoins sélectionnés'


class IsPermarentNeedy(admin.SimpleListFilter):
    title = 'nécessiteux permanent'
    parameter_name = 'permarent_needy'

    def lookups(self, request, model_admin):
        return (
            ('Oui', 'Oui'),
            ('Non', 'Non'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Oui':
            return queryset.filter(necessiteux__est_permanent=True)
        elif value == 'Non':
            return queryset.exclude(necessiteux__est_permanent=True)
        return queryset


@admin.register(Besoin)
class BesoinAdmin(admin.ModelAdmin):
    list_display = ["nom", "type", "est_urgent", "association"]
    date_hierarchy = "date_planification"
    search_fields = ["nom", "description"]
    list_filter = ["type", "est_urgent", "est_satisfait", "association", IsPermarentNeedy]
    actions = [satisfy_need, ]


@admin.register(Donneur)
class DonneurAdmin(admin.ModelAdmin):
    list_display = ["nom", "type", "active", "tel"]
    list_display_links = ["nom"]
    search_fields = ["nom", "tel"]
    list_filter = ["type", "active", "anonyme"]


@admin.register(AideRecu)
class AideRecuAdmin(admin.ModelAdmin):
    list_display = ["__str__", "donneur", "association"]
    date_hierarchy = "date_reception"
    list_filter = ["type", "association"]



