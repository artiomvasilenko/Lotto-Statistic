# Generated by Django 4.1 on 2023-05-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterstat', '0003_alter_lottery_options_alter_name_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]