from rest_framework import generics
from .serializers import DocumentSerializer, CategorySerializer
from .models import Document, Category


class DocumentListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
