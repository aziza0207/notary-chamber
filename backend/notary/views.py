from rest_framework import generics
from .serializers import NotarySerializer
from .models import Notary


class NotaryListAPIView(generics.ListAPIView):
    serializer_class = NotarySerializer
    queryset = Notary.objects.all()
