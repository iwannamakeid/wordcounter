# Generated by Django 2.2.1 on 2019-05-25 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
