from django.urls import path

from .views import (AphorismListAPIView, ContactListAPIView, DocumentListApiView, FAQListAPIView, LinksListAPIView,
                    NewsDetailAPIView, NewsListAPIView, NewsPinnedAPIView, PhotoSetDetailAPIView, PhotoSetListAPIView,
                    VideoListAPIView, SocialLinkListApiView)

app_name = 'content'

urlpatterns = [
    path('faq/', FAQListAPIView.as_view(), name='faq'),
    path('news/', NewsListAPIView.as_view(), name='news'),
    path('news-detail/<str:slug>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('news-pinned/', NewsPinnedAPIView.as_view(), name='pinned-news'),
    path('contacts/', ContactListAPIView.as_view(), name='contacts'),
    path('links/', LinksListAPIView.as_view(), name='links'),
    path('gallery-photo/', PhotoSetListAPIView.as_view(), name='gallery-photo'),
    path('gallery-photo/<str:slug>/', PhotoSetDetailAPIView.as_view(), name='gallery-photo'),
    path('gallery-video/', VideoListAPIView.as_view(), name='gallery-video'),
    path('aphorisms/', AphorismListAPIView.as_view(), name='aphorisms'),
    path('documents/', DocumentListApiView.as_view(), name='documents'),
    path('social-links/', SocialLinkListApiView.as_view(), name='social-links'),
]
