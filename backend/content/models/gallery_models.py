from django.db import models


def gallery_files(instance, filename):
    return f'gallery/photos/{filename}'


class PhotoSet(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField("Слаг", blank=True, null=True, db_index=True, unique=True)
    image = models.ImageField(upload_to=gallery_files, verbose_name='Обложка')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Фотосет'
        verbose_name_plural = 'Фотосеты'

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to=gallery_files, verbose_name='Изображение')
    photoset = models.ForeignKey('PhotoSet', verbose_name='Фотосет', related_name='photos', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.photoset} - фотографии'


class Video(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    link = models.URLField(max_length=300, verbose_name='Ссылка')
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title
