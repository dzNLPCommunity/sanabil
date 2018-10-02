from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve


from base import views as base_views
from base.views import contact_view, contact_success_view
from charity import views as charity_views
from Sanabil import settings
from charity.views import NecessiteuxListView, AideRecuListView, BesoinListView
from staff.views import AssociationListView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^associations/?', AssociationListView.as_view(), name='association-list'),
    url(r'^necessiteux/?', NecessiteuxListView.as_view(), name='necessiteux-list'),
    url(r'^besoins/?', BesoinListView.as_view(), name='besoin-list'),
    url(r'^aides/?', AideRecuListView.as_view(), name='aiderecu-list'),
    url(r'^help/?', charity_views.helppage, name='help-page'),
    url(r'^contact/', contact_view, name='contact-page'),
    url(r'^contact-success/', contact_success_view, name='contact-success-page'),
    url(r'^', charity_views.homepage, name='home-page'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns