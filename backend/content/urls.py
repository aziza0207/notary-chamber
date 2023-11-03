from django.urls import path
from .views import (FAQListAPIView,
                    NewsListAPIView,
                    NewsDetailAPIView,
                    NewsPinnedAPIView,
                    DocumentListAPIView,
                    LinksListAPIView,
                    PhotoListAPIView,
                    VideoListAPIView

                    )

urlpatterns = [
    path('documents/', DocumentListAPIView.as_view(), name='documents'),
    path('faq/', FAQListAPIView.as_view(), name='faq'),
    path('news/', NewsListAPIView.as_view(), name='news'),
    path('news-detail/<str:slug>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('news-pinned/', NewsPinnedAPIView.as_view(), name='pinned-news'),
    # path('news-recommended/', )
    path('links/', LinksListAPIView.as_view(), name='links'),
    path('gallery-photo/', PhotoListAPIView.as_view(), name='gallery-photo'),
    path('gallery-video/', VideoListAPIView.as_view(), name='gallery-video'),
]
