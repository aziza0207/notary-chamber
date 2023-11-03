from rest_framework import generics
from .serializers import NotarySerializer
from .models import Notary
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from notary.tasks import send_mail_delayed
from django.conf import settings
from .services import make_message
from .pagination import NotaryListPagination
from django.db.models import Q


class NotaryListAPIView(generics.ListAPIView):
    serializer_class = NotarySerializer
    
    pagination_class = NotaryListPagination
    
    def get_queryset(self):
        requested_page = self.request.query_params.get('page')
        value_to_search = self.request.query_params.get('search')
        queryset = Notary.objects.all()
        if requested_page == 'all':
            self.pagination_class = None
        if value_to_search:
            queryset = Notary.objects.filter(Q(full_name__icontains=value_to_search) | Q(city__icontains=value_to_search))
        return queryset


@csrf_exempt
def make_and_send_message(request):
    if request.method == 'POST':
        message = make_message(request)

        if settings.PRODUCTION:
            success = send_mail_delayed.delay(**message)
        else:
            success = send_mail(**message)

        if success:
            response = JsonResponse({'message': 'Message sended successfully'}, status=status.HTTP_202_ACCEPTED)
        else:
            response = JsonResponse({'message': 'Message failed to send'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return response
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
