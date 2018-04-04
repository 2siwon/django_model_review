from django.db import models

__all__ = (
    'Pizza',
    'Topping',
)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(
        'topping',
        blank=True,
    )

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
