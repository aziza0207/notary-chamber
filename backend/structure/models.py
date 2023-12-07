from django.db import models


def department_images(instance, filename):
    return f'structure/department/images/{filename}'


class AbstractDepartment(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    image = models.ImageField('Изображение', null=True, blank=True, upload_to=department_images)

    class Meta:
        ordering = ['id']
        abstract = True

    def __str__(self):
        return self.name


def department_worker_files(instance, filename):
    return f'structure/workers/{filename}'


class AbstractWorker(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=255, null=True, blank=True)
    image = models.ImageField('Изображение', null=True, blank=True, upload_to=department_worker_files)

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


class GeneralAssembly(AbstractDepartment):
    class Meta:
        verbose_name = 'Общее собрание'
        verbose_name_plural = 'Общие собрания'


class GeneralAssemblyWorker(AbstractWorker):
    department = models.ForeignKey('GeneralAssembly', verbose_name='Подразделение',
                                   related_name='workers', on_delete=models.CASCADE)


class NotaryCouncil(AbstractDepartment):
    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'


class NotaryCouncilWorker(AbstractWorker):
    department = models.ForeignKey('NotaryCouncil', verbose_name='Подразделение',
                                   related_name='workers', on_delete=models.CASCADE)


class Comission(AbstractDepartment):
    class Meta:
        verbose_name = 'Комиссия'
        verbose_name_plural = 'Комиссии'


class ComissionWorker(AbstractWorker):
    department = models.ForeignKey('Comission', verbose_name='Подразделение',
                                   related_name='workers', on_delete=models.CASCADE)
