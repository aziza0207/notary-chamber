from rest_framework import serializers

from ..models import Notary


class NotarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notary
        fields = ('id', 'full_name', 'photo', 'city', 'region', 'address', 'latitude', 'longitude',)
