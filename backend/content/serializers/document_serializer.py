from rest_framework import serializers

from ..models import Category, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'file')


class CategorySerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'documents',)
