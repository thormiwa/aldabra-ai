from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'booked_doctor_office',
        'appointment_for',
        'appointment_dt',
        'appointment_end_time',
        'appointment_state',
        'appointment_status',
        'booking_channel',
        'appointment_id'
    ]

    list_filter = [
        'patient',
        'booked_doctor_office',
        'appointment_for',
        'appointment_dt',
        'appointment_end_time',
        'appointment_state',
        'appointment_status',
        'booking_channel',
    ]

    list_per_page = 1000

    date_hierarchy = 'appointment_dt'

    time_hierarchy = 'appointment_dt'

    search_fields = [
        'patient',
        'booked_doctor_office',
        'appointment_for',
        'appointment_dt',
        'appointment_end_time',
        'appointment_state',
        'appointment_status',
        'booking_channel',
        'appointment_id'
    ]
