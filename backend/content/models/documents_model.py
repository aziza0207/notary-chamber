from django.db import models


def document_files(instance, filename):
    return f'documents/{filename}'


class Document(models.Model):
    title = models.CharField("Название", max_length=100)
    file = models.FileField("Файл", upload_to=document_files)

    class Meta:
        ordering = ["title"]
        verbose_name = "Документ"
        verbose_name_plural = "Все документы"

    def __str__(self):
        return self.title
