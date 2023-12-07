from rest_framework import serializers

from ..models import NotaryFlow, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name',)


class NotaryFlowSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = NotaryFlow
        fields = ('id', 'name', 'date_range', 'roles',)
