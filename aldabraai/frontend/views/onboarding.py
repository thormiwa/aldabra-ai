# common
from django.contrib import messages
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404
)

# decorators
from django.contrib.auth.decorators import (
    login_required,
    permission_required
)
from django.utils.text import slugify

# Models

# doctor models
from accounts.models import (
    Doctor,
)

# hospital models
from hospitals.models import (
    Hospital,
    DoctorID
)

# forms
from frontend.forms.onboarding import DoctorVerificationForm


# set residential hospital and verify ID
@login_required
def onboarding(request):

    user = request.user
    context = {
    }
    template_name = ''

    if user.is_doctor:
        template_name = 'onboarding/doctor_onboarding.html'
        if request.method == 'POST':
            verification_form = DoctorVerificationForm(request.POST)

            # check form validity
            if verification_form.is_valid():
                # get validated data
                data = {
                    'id': verification_form.cleaned_data['doctor_id'],
                    'residing_hospital': verification_form.cleaned_data['residing_hospital']
                }
                try:
                    # check id and hospital existence
                    id = DoctorID.objects.get(
                        name=user.full_name, doctor_id=data['id'], hospital=data['residing_hospital'])
                    if id:
                        doctor = Doctor.objects.create(
                            full_name=user.full_name,
                            doctor_id=data['id'],
                            residing_hospital=data['residing_hospital'],
                            owner=user,
                            slug=f"{'Dr_' + slugify(user.full_name)}")
                        doctor.save()
                        return redirect('frontend:dashboard')
                except DoctorID.DoesNotExist:
                    messages.error(
                        request, "does not match any Doctor ID or name, hospital to an ID, please contact your hospital admin")
                    context['verification_form'] = verification_form

            else:
                context['verification_form'] = verification_form

        else:
            verification_form = DoctorVerificationForm()
            context['verification_form'] = verification_form

    elif user.is_patient:
        return redirect('frontend:patient_create_view')

    return render(request, template_name, context)
