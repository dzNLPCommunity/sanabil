from dynamic_rest.serializers import DynamicModelSerializer

from staff.models import  Membre, Login, User, Role

class AgentSerializer(DynamicModelSerializer):
    class Meta:
        model = Membre
        fields = '__all__'


class RoleSerializer(DynamicModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class LoginSerializer(DynamicModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'


class UserSerializer(DynamicModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

