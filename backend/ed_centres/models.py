from django.db import models


def center_info(instance, filename):
    return f'center/info/{filename}'


class CenterInfo(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')
    thesis = models.TextField('Тезис')
    image = models.ImageField('Изображение', blank=True, null=True, upload_to=center_info)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - информация'
        verbose_name_plural = 'Обр. центры - информация'

    def __str__(self):
        return self.title


class CenterTask(models.Model):
    text = models.TextField('Формулировка')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - задача'
        verbose_name_plural = 'Обр. центры - задачи'

    def __str__(self):
        return f'{self.text[:27]}...' if len(self.text) > 30 else self.text


def center_management(instance, filename):
    return f'center/management/{filename}'


class ManagerProfile(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    text = models.TextField('Текст')
    image = models.ImageField('Изображение', blank=True, null=True, upload_to=center_management)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - руководитель'
        verbose_name_plural = 'Обр. центры - руководство'

    def __str__(self):
        return self.full_name


class StudyPlan(models.Model):
    title = models.CharField('Раздел', max_length=255)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - учебный план'
        verbose_name_plural = 'Обр. центры - учебные планы'

    def __str__(self):
        return self.title


class Discipline(models.Model):
    name = models.CharField('Название', max_length=255)
    content = models.TextField('Контент')
    study_plan = models.ForeignKey(to='StudyPlan', on_delete=models.CASCADE, verbose_name='Учебный план', related_name='disciplines')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - учебная дисциплина'
        verbose_name_plural = 'Обр. центры - учебные дисциплины'

    def __str__(self):
        return self.name


def center_staff(instance, filename):
    return f'center/staff/{filename}'


class TeachingStaff(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=255)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - преподаватель'
        verbose_name_plural = 'Обр. центры - преподаватели'

    def __str__(self):
        return self.full_name


class EducationalMaterial(models.Model):
    title = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обр. центры - учебный материал'
        verbose_name_plural = 'Обр. центры - учебные материалы'

    def __str__(self):
        return self.title
