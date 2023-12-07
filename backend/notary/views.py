from datetime import date

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.decorators import api_view

from notary.tasks import send_mail_delayed

from .models import Notary, NotaryFlow
from .pagination import NotaryListPagination
from .serializers import NotaryFlowSerializer, NotarySerializer
from .services import make_message


class NotaryFlowListAPIView(generics.ListAPIView):
    serializer_class = NotaryFlowSerializer
    queryset = NotaryFlow.objects.filter(date_start__gt=date.today())


class NotaryStatusListView(generics.ListAPIView):
    serializer_class = NotarySerializer
    pagination_class = NotaryListPagination

    def get_queryset(self):
        requested_status = self.request.query_params.get('status')
        queryset = Notary.objects.prefetch_related('assistants').filter(status=requested_status)
        return queryset


class NotaryListAPIView(generics.ListAPIView):
    serializer_class = NotarySerializer
    pagination_class = NotaryListPagination

    def get_queryset(self):
        requested_page = self.request.query_params.get('page')
        value_to_search = self.request.query_params.get('search')
        queryset = Notary.objects.prefetch_related('assistants')
        if requested_page == 'all':
            self.pagination_class = None
        if isinstance(value_to_search, str):
            if len(value_to_search) > 0:
                if value_to_search.isascii():
                    queryset = queryset.filter(Q(full_name_en__icontains=value_to_search) | Q(city_en__icontains=value_to_search))

                else:
                    queryset = queryset.filter(
                    Q(full_name_ru__icontains=value_to_search) | Q(city_ru__icontains=value_to_search))
            else:
                return queryset.none()
        return queryset
    

@api_view(['POST'])
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
