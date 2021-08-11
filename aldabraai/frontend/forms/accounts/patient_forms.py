
from django import forms

# models
from accounts.models import (
    Patient,
    PatientReview,
    PatientBankDetail,
    PatientInsuranceDetail,
)


class PatientCreationForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            'profile_picture',
            'full_name',
            'home_address',
            'city',
            'country',
            'phone',
            'family_or_emerg_phone'
        ]

    def __init__(self, *args, **kwargs):
        super(PatientCreationForm, self).__init__(*args, **kwargs)

        for field in (
            self.fields['full_name'],
            self.fields['home_address'],
            self.fields['city'],
            self.fields['country'],
            self.fields['phone'],
            self.fields['family_or_emerg_phone']
        ):
            field.widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )