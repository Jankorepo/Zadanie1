# Generated by Django 3.1.3 on 2021-01-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0008_czytelnik_kod_dostepu'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktualnewypozyczenia',
            name='kod_dostepu',
            field=models.IntegerField(default=0),
        ),
    ]
