from django.db import models
from django.urls import reverse


class Item(models.Model):
    """Модель товара."""
    CURRENCY = (
        ("rub", 'RUB'),
        ("usd", 'USD'),
    )
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=1,
                                verbose_name="Цена")
    currency = models.CharField(max_length=3,
                                choices=CURRENCY,
                                default="rub",
                                verbose_name="Валюта")

    @property
    def get_absolute_url(self):
        """Обратное построение адресов."""
        return reverse("view_item", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-id']


class Order(models.Model):
    """Модель заказа товара."""
    items = models.ManyToManyField(Item,
                                   verbose_name="Товары")

    def get_absolute_url(self):
        return reverse("view_order", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Заказ {self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-id']
