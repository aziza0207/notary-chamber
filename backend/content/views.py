from datetime import datetime

from rest_framework import generics

from .models import FAQ, Aphorism, Contact, Document, Link, News, PhotoSet, Video, SocialLink
from .pagination import NewsListPagination
from .serializers import (AphorismSerializer, ContactSerializer, DocumentSerializer, FAQSerializer, LinkSerializer,
                          NewsDetailSerializer, NewsListSerializer, PhotoSetDetailSerializer, PhotoSetListSerializer,
                          VideoSerializer, SocialLinkSerializer)


class SocialLinkListApiView(generics.ListAPIView):
    serializer_class = SocialLinkSerializer
    queryset = SocialLink.objects.all()


class DocumentListApiView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


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
        if isinstance(requested_title, str):
            if len(requested_title) > 0:
                queryset = queryset.filter(title__icontains=requested_title)
            else: 
                queryset = queryset.none()
        if isinstance(date_to_search, str):
            if len(date_to_search) > 0:
                cleaned_date = date_to_search.split(' GMT')[0]
                clean_date = datetime.strptime(cleaned_date, "%a %b %d %Y %H:%M:%S").date()
                queryset = queryset.filter(date=clean_date)
            else:
                queryset = queryset.none()
        return queryset


class NewsDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = NewsDetailSerializer

    def get_object(self):
        slug = self.kwargs['slug']
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
