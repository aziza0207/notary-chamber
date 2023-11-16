from django.db import models

from .schedule_abs_model import DayOffSchedule, WorkSchedule

# from location_field.models.plain import PlainLocationField


def notary_photos(instance, filename):
    return f'photos/{filename}'


class Notary(WorkSchedule, DayOffSchedule):
    full_name = models.CharField("Имя", max_length=100)
    city = models.CharField("Город", null=True, blank=True, max_length=150)

    phone = models.CharField("Номер телефона", max_length=30)
    email = models.EmailField("Email", null=True, blank=True)
    photo = models.ImageField("Фото", blank=True, null=True, upload_to=notary_photos)
    address = models.CharField("Адрес", max_length=255)
    region = models.CharField("Регион", null=True, blank=True)
    # notary_coordinates = PlainLocationField(based_fields=['city'], verbose_name="Координаты", blank=True)

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
