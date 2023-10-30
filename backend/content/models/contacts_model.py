from django.db import models


class Contact(models.Model):
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        ordering = ["id"]
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone
