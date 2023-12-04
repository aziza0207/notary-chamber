from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EdCentresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ed_centres'
    verbose_name = _('Ed_centres')
