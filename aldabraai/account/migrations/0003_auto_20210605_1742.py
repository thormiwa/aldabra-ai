# Generated by Django 3.2.4 on 2021-06-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='full_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Home Address'),
        ),
    ]