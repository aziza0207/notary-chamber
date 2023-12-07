import json

from django.conf import settings

from notary.models import EducationalCentre, NotaryFlow, Recipient, Role


def make_message(request):
    data = json.loads(request.body)
    role = int(data.get('role'))
    if role:
        recipients = EducationalCentre.objects.all()
        subject_role = Role.objects.get(id=role).name
        flow_id = data.get('flow')
        flow = NotaryFlow.objects.get(id=flow_id)
        subject = f'[{subject_role.upper()}]Заявка на обучение в центре'
        message = f'''Сведения о кандидате на обучение.
        \nИмя: {data.get('name')}.
        \nКонтакты: Телефон: {data.get('phone')}. Почта: {data.get('email')}.
        \nРоль: {subject_role}.
        \nВыбранный курс: {flow.name}, {flow.date_range}.'''
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
