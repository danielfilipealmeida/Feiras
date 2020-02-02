# Generated by Django 3.0.2 on 2020-01-28 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('coordinates', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feirasApp.Location')),
            ],
        ),
    ]
