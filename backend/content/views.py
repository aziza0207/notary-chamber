from rest_framework import generics

from .models import FAQ, Contact, Document, Link, News, PhotoSet, Video, Aphorism
from .pagination import NewsListPagination
from .serializers import (ContactSerializer, DocumentSerializer, FAQSerializer, LinkSerializer, NewsDetailSerializer,
                          NewsListSerializer, PhotoSetDetailSerializer, PhotoSetListSerializer, VideoSerializer,
                          AphorismSerializer)
from .search_servises import validate_search_parameter

from datetime import datetime

class AphorismListAPIView(generics.ListAPIView):
    serializer_class = AphorismSerializer
    queryset = Aphorism.objects.all()


class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    pagination_class = NewsListPagination

    def get_queryset(self):
        requested_title = self.request.query_params.get('title')
        date_to_search = self.request.query_params.get('date')
        queryset = News.objects.all()
        if requested_title:
            if validate_search_parameter(requested_title):
                queryset = queryset.filter(title__icontains=requested_title)
        elif date_to_search:
            if validate_search_parameter(date_to_search):
                cleaned_date = date_to_search.split(' GMT')[0]
                clean_date = datetime.strptime(cleaned_date, "%a %b %d %Y %H:%M:%S").date()
                queryset = queryset.filter(date=clean_date)
        return queryset


class NewsDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = NewsDetailSerializer

    def get_object(self):
        slug = self.kwargs["slug"]
        return News.objects.get(slug=slug)


class NewsPinnedAPIView(generics.ListAPIView):
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return News.objects.filter(is_pinned=True)[:2]


class LinksListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class PhotoSetListAPIView(generics.ListAPIView):
    serializer_class = PhotoSetListSerializer
    queryset = PhotoSet.objects.all()


class PhotoSetDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PhotoSetDetailSerializer
    queryset = PhotoSet.objects.all()
    lookup_field = 'slug'


class VideoListAPIView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class ContactListAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.filter(is_visible=True)
