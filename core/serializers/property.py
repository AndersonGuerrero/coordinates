from rest_framework.serializers import ModelSerializer

from core.models import Property


class PropertySerializer(ModelSerializer):

    class Meta:
        model = Property
        fields = ['id', 'name', 'full_limits', 'created_at']
