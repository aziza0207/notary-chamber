from django.db import models


def news_images(instance, filename):
    return f'news_images/{filename}'


class NewsImage(models.Model):
    image = models.ImageField('Изображение', blank=True, null=True, upload_to=news_images)
    news = models.ForeignKey('content.News', verbose_name='Новости', on_delete=models.CASCADE,
                             related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'Новости - {self.news.title}'


def news_main_image(instance, filename):
    return f'news_main_image/{filename}'


class News(models.Model):
    main_image = models.ImageField('Основное изображение', blank=True, null=True, upload_to=news_main_image)
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('Слаг', blank=True, null=True, db_index=True, unique=True)
    description = models.TextField('Текст')
    video = models.URLField('ССылка на видео', blank=True, null=True)
    date = models.DateField('Дата', auto_now_add=True, blank=True, null=True)
    is_pinned = models.BooleanField('Закрепленные', default=False)

    class Meta:
        ordering = ['-date',]
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title[:50] + '...'



