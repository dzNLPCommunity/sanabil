from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve


from base import views as base_views
from Sanabil import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^', base_views.index),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns