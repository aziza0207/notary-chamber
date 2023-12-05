from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class DaysChoice(TextChoices):
    PON = _("Понедельник"), "Понедельник"
    BT = _("Вторник"), "Вторник"
    SR = _("Среда"), "Среда"
    CT = _("Четверг"), "Четверг"
    PT = _("Пятница"), "Пятница"
    SB = _("Суббота"), "Суббота"
    VS = _("Воскресенье"), "Воскресенье"
