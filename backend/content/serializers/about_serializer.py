from rest_framework import serializers

from ..models import NotaryChamberDepartment, NotaryWorker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaryWorker
        fields = ('id', 'full_name', 'position',)


class DepatmentSerializer(serializers.ModelSerializer):
    workers = WorkerSerializer(many=True)
    class Meta:
        model = NotaryChamberDepartment
        fields = ('name', 'description', 'image', 'workers',)
