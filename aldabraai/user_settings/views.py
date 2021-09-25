## django builtin shortcuts
from django.shortcuts import (
    get_object_or_404,
    get_list_or_404,
    render
)
# decorators
from django.contrib.auth.decorators import login_required
# django view functions

# app models

@login_required
def settings_view(request):
    """
    get all user related objects
    first check user profile type

    if user.is_doctor return Doctor related objects
    if user.is_patient return Patient related objects
    """

    template_name = 'settings/'  # template name and path to rendered
    user = request.user  # user making request
    context = {'user': user}  # context data for data rendering

    if user.is_patient:
        template_name = template_name + 'patient_settings.html'
        context['profile'] = user.patient_profile
        #context['med_records'] = user.medicalrecord
        #context['bank_details'] = user.bank_details
        #context['insurrance_details'] = user.insurrance_details

    if user.is_doctor:
        template_name = template_name + 'doctor_settings.html'
        context['profile'] = user.doctor_profile
        #context['doctor_office'] = user.doctor_office
        #context['doctor_qual'] = user.doctor_qualifications
        #context['doctor_specs'] = user.doctor_specializations
        #context['affiliated_hosp'] = user.affiliated_hospitals

    return render(request, template_name, context=context)
