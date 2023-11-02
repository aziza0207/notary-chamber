from django.apps import AppConfig


class NotaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notary'

    def ready(self) -> None:
        import notary.signals
        return super().ready()
