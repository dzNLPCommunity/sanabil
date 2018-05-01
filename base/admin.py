from django.contrib import admin
from django.apps import apps

baseapp = apps.get_app_config('base')

for model in baseapp.get_models():
    admin.site.register(model)

from django.contrib.auth.models import Permission

admin.site.register(Permission)

