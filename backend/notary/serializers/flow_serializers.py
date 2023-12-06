from rest_framework import serializers
from ..models import NotaryFlow, MinistryFlow, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name',)


class NotaryFlowSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = NotaryFlow
        fields = ('id', 'date_range', 'roles',)


class MinistryFlowSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = MinistryFlow
        fields = ('id', 'date_range', 'roles',)
