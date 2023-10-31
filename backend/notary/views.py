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


class NotaryListAPIView(generics.ListAPIView):
    serializer_class = NotarySerializer
    queryset = Notary.objects.all()


def make_and_send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = f'''Сообщение от {data.get('name')}.
        \nКонтакты: email - {data.get('email')}.
        \nСообщение:
        \n"{data.get('text')}".'''
        success = send_mail_delayed.delay(message)
        if success:
            response = JsonResponse({'message': 'Message sended successfully'}, status=status.HTTP_202_ACCEPTED)
        else:
            response = JsonResponse({'message': 'Message failed to send'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return response
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
