from django.db import models


def content_docs(instance, filename):
    return f'content/documents/{filename}'


class Document(models.Model):
    title = models.CharField('Название', max_length=255)
    file = models.FileField('Файл', upload_to=content_docs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title
