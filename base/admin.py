from django.contrib import admin
from django.apps import apps

baseapp = apps.get_app_config('base')

for model in baseapp.get_models():
    admin.site.register(model)

from django.contrib.auth.models import Permission

admin.site.register(Permission)


admin.site.site_header = "Sanabil"
admin.site.site_title = "Sanabil"
admin.site.admin_name ='Unchained'

