from django.db import models


class EducationalFlow(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Поток на обучение'
        verbose_name_plural = 'Потоки на обучение'

    def __str__(self):
        return self.name