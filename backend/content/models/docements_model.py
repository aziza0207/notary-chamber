from django.db import models


class Category(models.Model):
    title = models.CharField("Название", max_length=100)

    class Meta:
        ordering = ["id"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


def document_files(instance, filename):
    return f'documents/{filename}'


class Document(models.Model):
    title = models.CharField("Название", max_length=20)
    file = models.FileField("Файл", upload_to=document_files)
    category = models.ForeignKey("Category", related_name="documents", on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title
