from django.core.mail import send_mail
import json
from django.conf import settings
from notary.models import Recipient

def make_message(request):
    data = json.loads(request.body)
    recipients = Recipient.objects.all()
    
    kwargs = {
    'message': f'''Сообщение от {data.get('name')}.
    \nКонтакты: Телефон - {data.get('phone')}.
    \nСообщение:
    \n"{data.get('text')}".''',
    
    'subject': 'New message from a client',
    'from_email': settings.EMAIL_HOST,
    'recipient_list': [recipient.email for recipient in recipients],
    'fail_silently': False
    }
    return kwargs
