from dynamic_rest.serializers import DynamicModelSerializer

from staff.models import  Membre, Login

class AgentSerializer(DynamicModelSerializer):
    class Meta:
        model = Membre
        fields = '__all__'


class LoginSerializer(DynamicModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'



