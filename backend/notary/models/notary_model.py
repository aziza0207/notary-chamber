from django.db import models
from ..constants import CityChoice, RegionChoice

def notary_photos(instance, filename):
    return f'photos/{filename}'


class Notary(models.Model):
    full_name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото", blank=True, null=True, upload_to=notary_photos)
    city = models.CharField("Город", choices=CityChoice.choices)
    address = models.CharField("Адрес", max_length=255)
    region = models.CharField("Регион", choices=RegionChoice.choices)
    latitude = models.CharField("Широта", default='Coordinates not defined', max_length=30)
    longitude = models.CharField("Долгота", default='Coordinates not defined', max_length=30)

    class Meta:
        ordering = ["id"]
        verbose_name = "Нотариус"
        verbose_name_plural = "Нотариусы"

    def __str__(self):
        return self.full_name
