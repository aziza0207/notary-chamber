import json

from django.conf import settings

from notary.models import Recipient, EducationalCentre
from notary.constants import RoleChoice, CentreChoice


def make_message(request):
    data = json.loads(request.body)
    # role = data.get('role')
    centre = data.get('centre')
    if centre:
        recipients = EducationalCentre.objects.all()
        # subject_role = RoleChoice[str(role).upper()]
        subject_centre = CentreChoice[str(centre).upper()]
        # subject = f'[{subject_role}][{subject_centre}]Заявка на обучение в центре'
                #\nРоль: {subject_role.label}.
        subject = f'[{subject_centre}]Заявка на обучение в центре'
        message = f'''Сведения о кандидате на обучение.
        \nИмя: {data.get('name')}.
        \nКонтакты: Телефон: {data.get('phone')}. Почта:{data.get('email')}.
        \nУчебный центр: {subject_centre.label}.'''
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
