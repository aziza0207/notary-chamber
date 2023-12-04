from django.urls import path

from .views import (CenterInfoListAPIView, CenterTaskListAPIView, ManagerProfileListAPIView,
                    StudyPlanListAPIView, TeachingStaffListAPIView, EducationalMaterialListAPIView)

app_name = 'ed_centres'

urlpatterns = [
    path('center-info/', CenterInfoListAPIView.as_view(), name='center-info'),
    path('center-tasks/', CenterTaskListAPIView.as_view(), name='center-tasks'),
    path('manager-profile/', ManagerProfileListAPIView.as_view(), name='manager-profile'),
    path('study-plan/', StudyPlanListAPIView.as_view(), name='study-plan'),
    path('teaching-staff/', TeachingStaffListAPIView.as_view(), name='teaching-staff'),
    path('educational-material/', EducationalMaterialListAPIView.as_view(), name='educational-material'),
]
