from django.conf import settings
from django.db import models
from .doctor import Doctor
from django.shortcuts import reverse

class Patient(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='patient_profile', on_delete=models.CASCADE)
    profile_picture = models.ImageField('Profile Picture', upload_to='uploads/imgs/dps/', blank=True) 
    full_name = models.CharField('Full Name', max_length=150, blank=True)
    home_address = models.CharField('Home Address', max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    phone = models.CharField('Phone Number', max_length=20, blank=True)
    family_or_emerg_phone = models.CharField('Family or Emergency Phone Number',max_length=20, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.full_name

    @property
    def patient_full_name(self):
        return self.owner.full_name

    def get_absolute_url(self):
        return reverse('accounts:patient-detail', kwargs={
                                                        'slug': self.slug
                                                        }
            )

