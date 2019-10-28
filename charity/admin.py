from django.apps import apps
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ExportMixin
from import_export.formats import base_formats
from charity.models import Famille, Necessiteux, Centre, Besoin, Donneur, AideRecu


@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):
    list_display = ["nom", "nombre_enfant"]
    list_display_links = ["nom"]
    search_fields = ["nom"]
    list_filter = ["nombre_enfant"]


class NecessiteuxResource(resources.ModelResource):
    class Meta:
        model = Necessiteux


@admin.register(Necessiteux)
class NecessiteuxAdmin(ExportActionModelAdmin):
    list_display = ["nom", "prenom", "tel", "association"]
    list_display_links = ["nom", "prenom"]
    search_fields = ["nom", "prenom", "tel"]
    list_filter = ['sexe', 'niveau_scolaire', 'pointure', 'taille', 'situation_familiale', 'situation_professionelle',
                   'est_orphelin', 'represent_famille', 'degré_nécessite', 'archivé', 'type']
    radio_fields = {'sexe': admin.HORIZONTAL, 'degré_nécessite': admin.HORIZONTAL}
    resource_class = NecessiteuxResource

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


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


class BesoinResource(resources.ModelResource):
    class Meta:
        model = Besoin


@admin.register(Besoin)
class BesoinAdmin(ExportActionModelAdmin):
    list_display = ["nom", "type", "est_urgent", "association"]
    date_hierarchy = "date_planification"
    search_fields = ["nom", "description"]
    list_filter = ["type", "est_urgent", "est_satisfait", "association", "type"]
    actions = [satisfy_need, ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "necessiteux":
            kwargs["queryset"] = Necessiteux.objects.filter(archivé=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    resource_class = BesoinResource

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


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
