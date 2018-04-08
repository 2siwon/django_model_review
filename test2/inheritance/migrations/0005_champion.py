# Generated by Django 2.0.4 on 2018-04-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0004_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_type', models.CharField(choices=[('magician', '마법사'), ('supporter', '서포터'), ('ad', '원거리 딜러')], max_length=20)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
