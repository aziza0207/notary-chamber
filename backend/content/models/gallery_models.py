from django.db import models


def gallery_files(instance, filename):
    return f'gallery/photos/{filename}'


class Photo(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(upload_to='gallery_files', verbose_name='Картинка')

    class Meta:
        ordering = ['id']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    link = models.URLField(max_length=300, verbose_name='Ссылка')

    class Meta:
        ordering = ['id']
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title
