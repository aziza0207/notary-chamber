from rest_framework import serializers

from ..models import Aphorism


class AphorismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aphorism
        fields = ('id', 'text',)
