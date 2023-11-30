from django.db import models


class Aphorism(models.Model):
    text = models.TextField('Текст')
    
    class Meta:
        verbose_name = 'Афоризм'
        verbose_name_plural = 'Афоризмы'

    def __str__(self):
        return f'{self.text[:27]}...' if len(self.text) > 30 else self.text
