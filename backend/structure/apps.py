from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StructureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'structure'
    verbose_name = _('Structure')
