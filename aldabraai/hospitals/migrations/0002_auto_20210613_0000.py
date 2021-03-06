# Generated by Django 3.2.4 on 2021-06-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorid',
            name='name',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctorid',
            name='position',
            field=models.CharField(blank=True, max_length=50, verbose_name='Position or Role in Hospital'),
        ),
    ]
