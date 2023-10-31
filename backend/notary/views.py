from rest_framework import generics
from .serializers import NotarySerializer
from .models import Notary
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


class NotaryListAPIView(generics.ListAPIView):
    serializer_class = NotarySerializer
    queryset = Notary.objects.all()


# @csrf_exempt
def perform_mailing(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = f'''Сообщение от {data.get('name')}.
        \nКонтакты: email - {data.get('email')}.
        \nСообщение:
        \n"{data.get('text')}".'''
        success = send_mail(
            subject='New message from a client',
            message=message,
            from_email='vlk@gmail.com',
            recipient_list=['valentine@mail.ru'],
            fail_silently=False
        )
        if success:
            response = JsonResponse({'message': 'Message sended successfully'}, status=status.HTTP_202_ACCEPTED)
        else:
            response = JsonResponse({'message': 'Message failed to send'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return response
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
