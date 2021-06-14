from django.db import models
from . import Hospital



class DoctorID(models.Model):
    name = models.CharField(max_length=35)
    doctor_id = models.CharField('ID', max_length=15)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    position = models.CharField('Position or Role in Hospital', max_length=50, blank=True)

    def __str__(self):
        return self.doctor_id

    class Meta:
        ordering = ['hospital']
        verbose_name = 'Doctor Hospital ID'
        verbose_name_plural = "Doctor Hospital IDs"