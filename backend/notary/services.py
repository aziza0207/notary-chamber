import json

from django.conf import settings

from notary.models import Recipient, EducationalCentre, Role
from notary.constants import CentreChoice


def make_message(request):
    data = json.loads(request.body)
    center = data.get('center')
    if center:
        role = int(data.get('role'))
        recipients = EducationalCentre.objects.all()
        subject_role = Role.objects.get(id=role).name
        subject_center = CentreChoice[str(center).upper()]
        subject = f'[{subject_role}][{subject_center}]Заявка на обучение в центре'
        message = f'''Сведения о кандидате на обучение.
        \nИмя: {data.get('name')}.
        \nКонтакты: Телефон: {data.get('phone')}. Почта: {data.get('email')}.
        \nРоль: {subject_role}.
        \nУчебный центр: {subject_center.label}.'''
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
