# django generic view classes
from django.views.generic import TemplateView

## models
from appointments.models import (
    Appointment
)
from auths.models import User
# user account models
from accounts.models import (
    Patient,
    Doctor
) 

# decorators
from django.contrib.auth.decorators import (
    login_required,
    permission_required
)

# helper/shortcut functions
from django.shortcuts import (
    get_object_or_404,
    render
)


@login_required()
def dashboard(request):
    user = request.user

    if user.is_patient:
        template_name = 'dashboards/patient_dashboard.html'

        context = {
            'user': user,
            'patient': Patient.objects.get(owner=user),
            'latest_appointments': Appointment.booked_appointments.filter(patient=user) 
        }

    elif user.is_doctor:
        template_name = 'dashboards/doctor_dashboard.html'
        
        context = {
            'user': user,
            'doctor': Doctor.objects.get(owner=user)
        }
        
    return render(request, template_name, context)

