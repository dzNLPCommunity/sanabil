from django.contrib import admin

from staff.models import Association, Membre, Login


@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ["nom", "prénom", "email", "tel"]
    search_fields = ["nom", "prénom", "email", "tel"]
    list_filter = ["profil"]

@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = ['nom', 'surnom', 'telephone', 'commune', 'website', 'responsable']
    list_display_links = ['nom','surnom']
    search_fields = ['nom', 'surnom', 'telephone']
    list_filter = ['commune__wilaya']


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
