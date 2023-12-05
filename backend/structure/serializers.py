from rest_framework import serializers

from .models import GeneralAssembly, GeneralAssemblyWorker, NotaryCouncil, NotaryCouncilWorker, Comission, ComissionWorker, NotaryCouncilDocument


class GeneralAssemblyWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralAssemblyWorker
        fields = ('id', 'full_name', 'position',)


class GeneralAssemblySerializer(serializers.ModelSerializer):
    workers = GeneralAssemblyWorkerSerializer(many=True)
    class Meta:
        model = GeneralAssembly
        fields = ('id', 'name', 'description', 'image', 'document', 'workers',)


class NotaryCouncilDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaryCouncilDocument
        fields = ('id', 'document',)


class NotaryCouncilWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaryCouncilWorker
        fields = ('id', 'full_name', 'position',)


class NotaryCouncilSerializer(serializers.ModelSerializer):
    workers = NotaryCouncilWorkerSerializer(many=True)
    documents = NotaryCouncilDocumentSerializer(many=True)
    class Meta:
        model = NotaryCouncil
        fields = ('id', 'name', 'description', 'image', 'documents', 'workers',)


class ComissionWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionWorker
        fields = ('id', 'full_name', 'position',)


class ComissionSerializer(serializers.ModelSerializer):
    workers = ComissionWorkerSerializer(many=True)
    class Meta:
        model = Comission
        fields = ('id', 'name', 'description', 'image', 'document', 'workers',)



# class DepatmentSerializer(serializers.ModelSerializer):
#     workers = WorkerSerializer(many=True)
#     # description = serializers.SerializerMethodField()
#     # desc_list = serializers.SerializerMethodField()
#     class Meta:
#         model = NotaryChamberDepartment
#         fields = ('name', 'description', 'image', 'workers',)

    # def get_descriprion(self, obj):
    #     if ':\r\n' in obj.description and (';\r\n2)' in obj.description or ';\r\n-' in obj.description):
    #         global list_begins
    #         list_begins = obj.description.find(';\r\n1)')
    #         list_begins = list_begins if list_begins else obj.description.find(';\r\n-')
    #         return obj.description[:list_begins]
    #     else:
    #         return obj.description

    # def get_list(self, obj):
    #     if list_begins:
    #         list_ends
    #         return obj.description[list_begins:]
