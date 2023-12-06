from django.db.models import TextChoices


class CentreChoice(TextChoices):
    MINISTRY_CENTRE = ('МИНИСТЕРСТВО', 'Министерство')
    NOTARY_CENTRE = ('НОТАРИАЛЬНЫЙ ЦЕНТР', 'Нотариальный центр')
