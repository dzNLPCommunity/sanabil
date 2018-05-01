from django.contrib import admin

from django.apps import apps

notification_app = apps.get_app_config('notification')

for model in notification_app.get_models():
    admin.site.register(model)
