from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Доступная роль'
        verbose_name_plural = 'Доступные роли'

    def __str__(self):
        return self.name


class EducationalFlowAbstractModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название')
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания')

    def _date_range(self):
        return f'{self.date_start.strftime("%d.%m.%Y")} - {self.date_end.strftime("%d.%m.%Y")}'

    _date_range.short_description = 'Сроки'

    date_range = property(_date_range)

    class Meta:
        abstract = True
        ordering = ['-id']

    def __str__(self):
        return self.name


class NotaryFlow(EducationalFlowAbstractModel):
    roles = models.ManyToManyField(to='Role', related_name='notary_flows', verbose_name='Роли', blank=True)

    class Meta:
        verbose_name = 'Поток в нотариальный центр'
        verbose_name_plural = 'Потоки в нотариальный центр'
