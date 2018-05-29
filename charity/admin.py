from django.apps import apps
from django.contrib import admin



donationapp = apps.get_app_config('charity')

for model in donationapp.get_models():
    admin.site.register(model)


