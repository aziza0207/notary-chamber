from django.urls import path
from .views import DocumentListAPIView, NewsListAPIView, NewsDetailAPIView, NewsPinnedAPIView

urlpatterns = [
    path('documents/', DocumentListAPIView.as_view(), name='documents'),
    path('news/', NewsListAPIView.as_view(), name='news'),
    path('news-detail/<str:slug>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('news-pinned/', NewsPinnedAPIView.as_view(), name='pinned-news')

]
