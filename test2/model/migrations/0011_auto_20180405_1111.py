# Generated by Django 2.0.4 on 2018-04-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0010_auto_20180405_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='recommender',
        ),
        migrations.AddField(
            model_name='membership',
            name='recommenders',
            field=models.ManyToManyField(blank=True, related_name='recommenders_membership_set', to='model.Idol'),
        ),
    ]
