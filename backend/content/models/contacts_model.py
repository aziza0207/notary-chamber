from django.db import models


class LinkTypeChoices(models.TextChoices):
    Yt = "YouTube", "YouTube"
    FB = "Facebook", "Facebook"
    IG = "Instagram", "Instagram"


class Contact(models.Model):
    phone = models.CharField("Телефон", max_length=30)
    is_visible = models.BooleanField(default=False, verbose_name="Виден на сайте")

    class Meta:
        ordering = ["id"]
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone


class SocialLink(models.Model):
    type = models.CharField("Тип", max_length=150, choices=LinkTypeChoices.choices)
    link = models.CharField("Ссылка", max_length=255)

    class Meta:
        ordering = ["id"]
        verbose_name = "Контакт (ссылка)"
        verbose_name_plural = "Контакты (ссылки)"

    def __str__(self):
        return self.link
