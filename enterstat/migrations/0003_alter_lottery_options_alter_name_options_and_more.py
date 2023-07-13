# Generated by Django 4.1 on 2023-05-08 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterstat', '0002_name_jackpot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lottery',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='name',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='lottery',
            name='date',
            field=models.DateField(default=datetime.date(2023, 5, 8), verbose_name='Дата розыгрыша'),
        ),
    ]
