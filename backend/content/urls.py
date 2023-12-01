from django.urls import path

from .admin.views import upload_photo
from .views import (ContactListAPIView, FAQListAPIView, LinksListAPIView, NewsDetailAPIView,
                    NewsListAPIView, NewsPinnedAPIView, PhotoSetDetailAPIView, PhotoSetListAPIView, VideoListAPIView,
                    AphorismListAPIView, CenterInfoListAPIView, CenterTaskListAPIView, ManagerProfileListAPIView,
                    StudyPlanListAPIView, TeachingStaffListAPIView, EducationalMaterialListAPIView)

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
    path('upload_photo/', upload_photo, name='upload_photo'),
    path('aphorisms/', AphorismListAPIView.as_view(), name='aphorisms'),
    path('center-info/', CenterInfoListAPIView.as_view(), name='center-info'),
    path('center-tasks/', CenterTaskListAPIView.as_view(), name='center-tasks'),
    path('manager-profile/', ManagerProfileListAPIView.as_view(), name='manager-profile'),
    path('study-plan/', StudyPlanListAPIView.as_view(), name='study-plan'),
    path('teaching-staff/', TeachingStaffListAPIView.as_view(), name='teaching-staff'),
    path('educational-material/', EducationalMaterialListAPIView.as_view(), name='educational-material'),
]
