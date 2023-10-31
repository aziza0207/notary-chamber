from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_mail_delayed(message):
    send_mail(
            subject='New message from a client',
            message=message,
            from_email='vlk@gmail.com',
            recipient_list=['valentine@mail.ru'],
            fail_silently=False
        )
