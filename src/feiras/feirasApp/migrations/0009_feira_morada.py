src/feiras/feirasApp/migrations/0009_feira_morada.py # Generated by Django 3.0.2 on 2020-02-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feirasApp', '0008_auto_20200202_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='feira',
            name='morada',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
