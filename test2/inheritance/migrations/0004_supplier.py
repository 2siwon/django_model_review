# Generated by Django 2.0.4 on 2018-04-08 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0003_auto_20180407_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inheritance.Place')),
                ('customer', models.ManyToManyField(related_name='customer_place_set', to='inheritance.Place')),
            ],
            bases=('inheritance.place',),
        ),
    ]