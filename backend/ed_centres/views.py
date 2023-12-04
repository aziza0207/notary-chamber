from rest_framework import generics

from .models import CenterInfo, CenterTask, ManagerProfile, StudyPlan, TeachingStaff, EducationalMaterial
from .serializers import (CenterInfoSerializer, CenterTaskSerializer, ManagerProfileSerializer,
                          StudyPlanSerializer, TeachingStaffSerializer, EducationalMaterialSerializer)


class CenterInfoListAPIView(generics.ListAPIView):
    serializer_class = CenterInfoSerializer
    queryset = CenterInfo.objects.all()


class CenterTaskListAPIView(generics.ListAPIView):
    serializer_class = CenterTaskSerializer
    queryset = CenterTask.objects.all()


class ManagerProfileListAPIView(generics.ListAPIView):
    serializer_class = ManagerProfileSerializer
    queryset = ManagerProfile.objects.all()


class StudyPlanListAPIView(generics.ListAPIView):
    serializer_class = StudyPlanSerializer
    queryset = StudyPlan.objects.all()


class TeachingStaffListAPIView(generics.ListAPIView):
    serializer_class = TeachingStaffSerializer
    queryset = TeachingStaff.objects.all()


class EducationalMaterialListAPIView(generics.ListAPIView):
    serializer_class = EducationalMaterialSerializer
    queryset = EducationalMaterial.objects.all()
