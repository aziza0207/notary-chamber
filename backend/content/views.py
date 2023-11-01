from rest_framework import generics
from .serializers import CategorySerializer, NewsListSerializer, NewsDetailSerializer, FAQSerializer
from .models import Category, News, FAQ


class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

class DocumentListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()


class NewsDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = NewsDetailSerializer

    def get_object(self):
        slug = self.kwargs["slug"]
        return News.objects.filter(slug=slug).first()


class NewsPinnedAPIView(generics.ListAPIView):
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return News.objects.filter(is_pinned=True)[:2]
