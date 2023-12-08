from django.db import models

from notary.constants import StatusChoice

from .schedule_abs_model import DayOffSchedule, WorkSchedule

# from location_field.models.plain import PlainLocationField


class Notary(WorkSchedule, DayOffSchedule):
    full_name = models.CharField('Имя', max_length=100)
    city = models.CharField('Город', null=True, blank=True, max_length=150)
    status = models.CharField('Статус', max_length=50, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)
    phone = models.CharField('Номер телефона', max_length=30)
    email = models.EmailField('Email', null=True, blank=True)
    address = models.CharField('Адрес', max_length=255)
    region = models.CharField('Регион', null=True, blank=True)
    # notary_coordinates = PlainLocationField(based_fields=['city'], verbose_name="Координаты", blank=True)

    latitude = models.CharField('Широта', default='Coordinates not defined', blank=True, max_length=30)
    longitude = models.CharField('Долгота', default='Coordinates not defined', blank=True, max_length=30, help_text=
    '''Пустые поля координат заполняются автоматически.
                                Автоматическое определение может давать некорректный результат,
                                рекомендуется проверять полученные координаты.
                                ''')

    class Meta:
        ordering = ['id']
        verbose_name = 'Нотариус'
        verbose_name_plural = 'Нотариусы'

    def __str__(self):
        return self.full_name


class Assistant(models.Model):
    full_name = models.CharField('Имя', max_length=100)
    notary = models.ForeignKey('Notary', verbose_name='Нотариус', related_name='assistants', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Ассистент'
        verbose_name_plural = 'Ассистенты'

    def __str__(self):
        return self.full_name
