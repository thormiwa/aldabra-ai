# django form class
from django import forms
from django.forms import ModelForm, fields

# doctor model
from accounts.models import Doctor

# User Model
from django.conf import settings

class DoctorVerificationForm(ModelForm):
    owner = forms.ChoiceField(choices=settings.AUTH_USER_MODEL, widget=forms.HiddenInput, disabled=True, required=False)

    class Meta:
        model = Doctor
        fields = [
            'full_name',
            'residing_hospital',
            'doctor_id',
            'owner'
        ]

    
    def __init__(self, *args, **kwargs):
        """
        specify class name
        """

        super(DoctorVerificationForm, self).__init__(*args, **kwargs)
        for fields in (
            self.fields['full_name'],
            self.fields['doctor_id'],  
            self.fields['residing_hospital']):
            fields.widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )