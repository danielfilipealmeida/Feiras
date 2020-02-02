# Generated by Django 3.0.2 on 2020-02-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feirasApp', '0004_feira_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='feira',
            name='dia',
            field=models.IntegerField(choices=[(1, 'Domingo'), (2, 'Segunda'), (3, 'Terca'), (4, 'Quarta'), (5, 'Quinta'), (6, 'Sexta'), (7, 'Sabado')], null=True),
        ),
        migrations.AddField(
            model_name='feira',
            name='semana',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
