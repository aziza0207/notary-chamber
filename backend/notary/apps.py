from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notary'
    verbose_name = _('Notary')

    def ready(self) -> None:
        import notary.signals
        return super().ready()
