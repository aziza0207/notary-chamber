from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class StatusChoice(TextChoices):
    ACTIVE = ("active", _("Действующий"))
    PAUSED = ("paused", _("Временно не работает"))
    FINISHED = ("finished", _("Завершил деятельность"))
