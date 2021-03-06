from django.db import models
from django.conf import settings
from hospitals.models import Hospital
from django.shortcuts import reverse


class Doctor(models.Model):
    profile_picture = models.ImageField('Profile Picture', width_field=120, height_field=80, blank=True)
    full_name = models.CharField(max_length=300, blank=True)
    doctor_id = models.CharField('Doctors ID', max_length=10, unique=True)
    residing_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    practicing_from = models.DateField(blank=True, null=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='doctor_profile', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    @property
    def doctor_full_name(self):
        return self.owner.full_name

    def get_absolute_url(self):
        return reverse('accounts:doctor-detail', kwargs={
                                                        'slug': self.slug}                                
            )

    def add_review_url(self):
        return reverse('accounts:doctor-review', kwargs={'slug': self.slug})
        
    class Meta:
        ordering = ['residing_hospital']

class AffiliatedHospital(models.Model):
    affiliated_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='affiliated_hospitals', on_delete=models.CASCADE) 
    hospital_name = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    affiliation_relationship = models.CharField(max_length=500, help_text='What relationship do have with the hospital, what do you or did you do there?')
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.affiliated_doctor


