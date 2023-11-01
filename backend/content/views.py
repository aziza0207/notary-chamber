from rest_framework import generics
from .serializers import FAQSerializer
from .models import Document, Category, FAQ


# class DocumentListAPIView(generics.ListAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
