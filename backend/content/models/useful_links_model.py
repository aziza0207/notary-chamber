from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    link = models.URLField(max_length=300, verbose_name='Ссылка')

    class Meta:
        ordering = ['id']
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'

    def __str__(self):
        return self.name
