from django.db import models


class Recipient(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'

    def __str__(self):
        return self.name


class EducationalCentre(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Обработчик образовательного центра'
        verbose_name_plural = 'Обработчики образовательного центра'

    def __str__(self):
        return self.name
