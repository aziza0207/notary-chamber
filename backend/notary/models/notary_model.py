from django.db import models

from ..constants import RegionChoice


def notary_photos(instance, filename):
    return f'photos/{filename}'


class Notary(models.Model):
    full_name = models.CharField("Имя", max_length=100)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True,  verbose_name="Город")
    phone = models.CharField("Номер телефона", max_length=30)
    photo = models.ImageField("Фото", blank=True, null=True, upload_to=notary_photos)
    address = models.CharField("Адрес", max_length=255)
    region = models.CharField("Регион", choices=RegionChoice.choices)
    latitude = models.CharField("Широта", default='Coordinates not defined', blank=True, max_length=30)
    longitude = models.CharField("Долгота", default='Coordinates not defined', blank=True, max_length=30, help_text=
    '''Пустые поля координат заполняются автоматически.
                                Автоматическое определение может давать некорректный результат,
                                рекомендуется проверять полученные координаты.
                                ''')

    class Meta:
        ordering = ["id"]
        verbose_name = "Нотариус"
        verbose_name_plural = "Нотариусы"

    def __str__(self):
        return self.full_name


class City(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        ordering = ["id"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name




