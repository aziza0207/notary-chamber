from rest_framework import generics
from .serializers import DocumentSerializer
from .models import Document


class DocumentListAPIView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
