from django.contrib import admin

from django.apps import apps


staffapp = apps.get_app_config('staff')

for model in staffapp.get_models():
    if model not in []:
        admin.site.register(model)




