from django.db import models

__all__ = (
    'Idol',
    'Group',
    'MemberShip',
    'Entertainnment',
)


class Entertainnment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Idol(models.Model):
    name = models.CharField(max_length=30)
    entertainment = models.ForeignKey(
        'Entertainnment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} - {self.entertainment.name}'


class Group(models.Model):
    name = models.CharField(max_length=30)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='MemberShip',
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class MemberShip(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # Idol 테이블의 어떤 행이 지워지면 그 아이돌을 참조하는 Membership 테이블의 row도 모두 삭제된다.
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set',
    )
    recommender = models.ForeignKey(
        Idol,
        null=True,
        on_delete=models.SET_NULL,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        is_active = 'X'
        if self.is_active:
            is_active = 'O'

        return f'{self.group.name} - ' \
               f'{self.idol.name}' \
               f'({is_active})'
