from django.db import models


def department_files(instance, filename):
    return f'department/{filename}'


class NotaryChamberDepartment(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    image = models.ImageField('Изображение', null=True, blank=True, upload_to=department_files)

    class Meta:
        ordering = ['id']
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


class NotaryWorker(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=255, null=True, blank=True)
    department = models.ForeignKey('NotaryChamberDepartment', verbose_name='Подразделение',
                                   related_name='workers', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name
