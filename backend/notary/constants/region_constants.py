from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class RegionChoice(TextChoices):
    DJALAL_ABAD = ("Djalal_Abad", _("Джалал-Абад"))
    BISHKEK = ("Bishkek", _("Бишкек"))
    KANT = ("Каnt", _("Кант"))



