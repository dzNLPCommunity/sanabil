from dynamic_rest.serializers import DynamicModelSerializer

from notification.models import Notification


class NotificationSerializer(DynamicModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
