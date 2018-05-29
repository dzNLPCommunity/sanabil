"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import debug_toolbar
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework import routers



from base import views as base_views
from staff import views  as staff_views

from notification import views as notification_views


from Sanabil import settings


router = routers.DefaultRouter()


router.register(r'auth/groups', base_views.GroupViewSet)
router.register(r'auth/permissions', base_views.PermissionViewSet)



router.register(r'base/wilayas', base_views.WilayaViewSet)
router.register(r'base/communes', base_views.CommuneViewSet)
router.register(r'base/parameters', base_views.ParameterViewSet)


router.register(r'staff/agents', staff_views.AgentViewSet)
router.register(r'staff/logins', staff_views.LoginViewSet)


router.register(r'notification/notifications', notification_views.NotificationViewSet)

router.register(r'fcm/devices', FCMDeviceAuthorizedViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^authenticate/', base_views.CustomObtainAuthToken.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^', base_views.index),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns