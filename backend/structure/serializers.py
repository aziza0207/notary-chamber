from rest_framework import serializers

from .models import (Comission, ComissionWorker, GeneralAssembly, GeneralAssemblyWorker, NotaryCouncil,
                     NotaryCouncilWorker)


class GeneralAssemblyWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralAssemblyWorker
        fields = ('id', 'full_name', 'position', 'image',)


class GeneralAssemblySerializer(serializers.ModelSerializer):
    workers = GeneralAssemblyWorkerSerializer(many=True)
    class Meta:
        model = GeneralAssembly
        fields = ('id', 'name', 'description', 'image', 'workers',)


class NotaryCouncilWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaryCouncilWorker
        fields = ('id', 'full_name', 'position', 'image',)


class NotaryCouncilSerializer(serializers.ModelSerializer):
    workers = NotaryCouncilWorkerSerializer(many=True)
    class Meta:
        model = NotaryCouncil
        fields = ('id', 'name', 'description', 'image', 'workers',)


class ComissionWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionWorker
        fields = ('id', 'full_name', 'position', 'image',)


class ComissionSerializer(serializers.ModelSerializer):
    workers = ComissionWorkerSerializer(many=True)
    class Meta:
        model = Comission
        fields = ('id', 'name', 'description', 'image', 'workers',)
