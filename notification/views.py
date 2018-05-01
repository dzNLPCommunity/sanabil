from dynamic_rest.viewsets import DynamicModelViewSet

from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationViewSet(DynamicModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

