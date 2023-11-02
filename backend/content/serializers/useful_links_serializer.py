from rest_framework import serializers

from content.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'name', 'link',)
