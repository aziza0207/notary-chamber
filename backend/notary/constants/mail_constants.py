from django.db.models import TextChoices


class RoleChoice(TextChoices):
    NOTARY = ('НОТАРИУС', 'Нотариус')
    ASSISTANT = ('АССИСТЕНТ', 'Ассистент')


class CentreChoice(TextChoices):
    MINISTRY_CENTRE = ('МИНИСТЕРСТВО', 'Министерство')
    NOTARY_CENTRE = ('НОТАРИАЛЬНЫЙ ЦЕНТР', 'Нотариальный центр')
