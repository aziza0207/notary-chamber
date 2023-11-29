from rest_framework import generics
from .serializers import GeneralAssemblySerializer, NotaryCouncilSerializer, ComissionSerializer
from .models import GeneralAssembly, NotaryCouncil, Comission
                          
class GeneralAssemblyListAPIView(generics.ListAPIView):
    serializer_class = GeneralAssemblySerializer
    queryset = GeneralAssembly.objects.all()


class NotaryCouncilListAPIView(generics.ListAPIView):
    serializer_class = NotaryCouncilSerializer
    queryset = NotaryCouncil.objects.all()


class ComissionListAPIView(generics.ListAPIView):
    serializer_class = ComissionSerializer
    queryset = Comission.objects.all()
