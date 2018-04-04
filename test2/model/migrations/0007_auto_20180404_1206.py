# Generated by Django 2.0.4 on 2018-04-04 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friends', models.ManyToManyField(blank=True, related_name='_twitteruser_friends_+', to='model.TwitterUser')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='model.User'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='model.Topping'),
        ),
    ]
