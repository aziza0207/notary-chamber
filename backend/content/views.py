from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import FAQ, Contact, Document, Link, News, PhotoSet, Video
from .pagination import NewsListPagination
from .serializers import (ContactSerializer, DocumentSerializer, FAQSerializer,
                          LinkSerializer, NewsDetailSerializer,
                          NewsListSerializer, PhotoSetDetailSerializer,
                          PhotoSetListSerializer, VideoSerializer)
from .services import make_creation_args


@csrf_exempt
def upload_photo(request):
    '''
    The function processes POST requests from admin inline models containing multiple files
    in request.FILES. The request.FILES also includes a collection named 'json_data' representing
    the parameters necessary for object creation.
    '''
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        parameters_str = request.FILES.get('json_data').read().decode()
        inline_model_class, create_args = make_creation_args(parameters_str)
        for file in files:
            inline_model_class.objects.create(image=file, **create_args)


class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class DocumentListAPIView(generics.ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        value_to_search = self.request.query_params.get('search')
        if isinstance(value_to_search, str):
            if len(value_to_search) > 0:
                queryset = queryset.filter(title_ru__icontains=value_to_search)
            else:
                return []
        return queryset


class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = NewsListPagination


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
