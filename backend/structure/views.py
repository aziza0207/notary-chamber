from rest_framework import generics

from .models import Comission, GeneralAssembly, NotaryCouncil
from .serializers import ComissionSerializer, GeneralAssemblySerializer, NotaryCouncilSerializer


class GeneralAssemblyListAPIView(generics.ListAPIView):
    serializer_class = GeneralAssemblySerializer
    queryset = GeneralAssembly.objects.prefetch_related('workers').all()


class NotaryCouncilListAPIView(generics.ListAPIView):
    serializer_class = NotaryCouncilSerializer
    queryset = NotaryCouncil.objects.prefetch_related('workers').all()


class ComissionListAPIView(generics.ListAPIView):
    serializer_class = ComissionSerializer
    queryset = Comission.objects.prefetch_related('workers').all()
