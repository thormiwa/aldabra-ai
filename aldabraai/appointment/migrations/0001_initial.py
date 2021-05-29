# Generated by Django 3.2 on 2021-04-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('appointment_for', models.CharField(blank=True, max_length=500)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('appointment_time', models.TimeField(blank=True, null=True)),
                ('appointment_end_time', models.TimeField(blank=True, null=True)),
                ('appointment_state', models.CharField(choices=[('RE', 'Requested'), ('AC', 'Accepted'), ('DE', 'Declined')], default='RE', max_length=10)),
                ('short_note', models.CharField(blank=True, max_length=500)),
                ('appointment_status', models.CharField(choices=[('DU', 'Due'), ('TK', 'Taken')], default='DU', max_length=5)),
                ('booking_channel', models.CharField(choices=[('OP', 'App'), ('OC', 'Call')], default='OP', max_length=5)),
                ('appointment_id', models.UUIDField(blank=True, null=True, unique=True)),
                ('doctor_dec_reason', models.CharField(blank=True, max_length=450, verbose_name="Doctor's Reason for Declining Appointment")),
                ('booked', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-appointment_date'],
            },
        ),
    ]
