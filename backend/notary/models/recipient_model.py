from django.db import models


class Recipient(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Получатель обращений граждан'
        verbose_name_plural = 'Получатели обращений граждан'

    def __str__(self):
        return self.name


class EducationalCentre(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Получатель заявок на обучение'
        verbose_name_plural = 'Получатели заявок на обучение'

    def __str__(self):
        return self.name
