from django.urls import path

from .admin.views import upload_photo
from .views import (ContactListAPIView, DocumentListAPIView, FAQListAPIView, LinksListAPIView, NewsDetailAPIView,
                    NewsListAPIView, NewsPinnedAPIView, PhotoSetDetailAPIView, PhotoSetListAPIView, VideoListAPIView,
                    DepartmentListAPIView)

app_name = 'content'

urlpatterns = [
    path('documents/', DocumentListAPIView.as_view(), name='documents'),
    path('faq/', FAQListAPIView.as_view(), name='faq'),
    path('news/', NewsListAPIView.as_view(), name='news'),
    path('news-detail/<str:slug>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('news-pinned/', NewsPinnedAPIView.as_view(), name='pinned-news'),
    path('contacts/', ContactListAPIView.as_view(), name='contacts'),
    path('links/', LinksListAPIView.as_view(), name='links'),
    path('gallery-photo/', PhotoSetListAPIView.as_view(), name='gallery-photo'),
    path('gallery-photo/<str:slug>/', PhotoSetDetailAPIView.as_view(), name='gallery-photo'),
    path('gallery-video/', VideoListAPIView.as_view(), name='gallery-video'),
    path('upload_photo/', upload_photo, name='upload_photo'),
    path('departments/', DepartmentListAPIView.as_view(), name='departments')
]
