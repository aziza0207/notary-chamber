from decouple import config
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

DEFAULT_ADMIN_NAME = config('DEFAULT_ADMIN_NAME')
DEFAULT_ADMIN_PASSWORD = config('DEFAULT_ADMIN_PASSWORD')
DEFAULT_ADMIN_EMAIL = config('DEFAULT_ADMIN_EMAIL')


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        if not user.objects.filter(username=DEFAULT_ADMIN_NAME).first():
            get_user_model().objects.create_superuser(username=DEFAULT_ADMIN_NAME,
                                                      password=DEFAULT_ADMIN_PASSWORD,
                                                      email=DEFAULT_ADMIN_EMAIL)
