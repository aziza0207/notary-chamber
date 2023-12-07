from django.db.models import TextChoices


class RegionChoice(TextChoices):
    DJALAL_ABAD = ("Djalal_Abad", "Джалал-Абад")
    BISHKEK = ("Bishkek", "Бишкек")
    KANT = ("Каnt", "Кант")
