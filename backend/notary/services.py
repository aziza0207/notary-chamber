import json

from django.conf import settings

from notary.models import Recipient, EducationalCentre
from notary.constants import RoleChoice, CentreChoice


def make_message(request):
    data = json.loads(request.body)
    role = data.get('role')
    if role:
        centre = data.get('centre')
        recipients = EducationalCentre.objects.all()
        subject = f'[{RoleChoice[str(role).upper()]}][{CentreChoice[str(centre).upper()]}]Заявка на обучение в центре'
        message = f'''Сведения о кандидате на обучение.
        \nИмя: {data.get('name')}.
        \nКонтакты: Телефон: {data.get('phone')}. Почта:{data.get('email')}.
        \nРоль {role}.
        \nУчебный центр: {centre}.'''
    else:
        recipients = Recipient.objects.all()
        subject = 'Новое сообщение от клиента'
        message = f'''Сообщение от {data.get('name')}.
        \nКонтакты: Телефон - {data.get('phone')}.
        \nСообщение:
        \n"{data.get('text')}".'''

    kwargs = {
    'message': message,
    'subject': subject,
    'from_email': settings.EMAIL_HOST,
    'recipient_list': [recipient.email for recipient in recipients],
    'fail_silently': False
    }

    return kwargs
