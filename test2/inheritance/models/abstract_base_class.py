from django.db import models

__all__ = (
    'School',
    'CommonInfo',
    'Student',
    'Teacher',
)


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    school = models.ForeignKey(
        School,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_set',

    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.name} - {self.home_group}'


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name } - {self.subject}'