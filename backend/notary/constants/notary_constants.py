from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class StatusChoice(TextChoices):
    ACTIVE = ("active", _("Действующий"))
    FINISHED = ("finished", _("Завершил деятельность"))
