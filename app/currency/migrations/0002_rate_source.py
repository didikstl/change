# Generated by Django 4.2.7 on 2023-11-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.CharField(default='privat', max_length=255),
            preserve_default=False,
        ),
    ]
