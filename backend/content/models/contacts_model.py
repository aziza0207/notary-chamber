from django.db import models


class Contact(models.Model):
    phone = models.CharField("Телефон", max_length=30)
    is_visible = models.BooleanField(default=False, verbose_name="Виден на сайте")

    class Meta:
        ordering = ["id"]
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone
