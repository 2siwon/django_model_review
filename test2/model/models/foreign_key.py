from django.db import models

__all__ = (
    'Car',
    'Manufacturer',
    'User',
)


class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer', on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.teacher and self.teacher.pk == self.pk:
            self.teacher = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f'내 이름 : {self.name}'
