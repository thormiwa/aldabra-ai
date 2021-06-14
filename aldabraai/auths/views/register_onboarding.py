# django builtin required library
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login
)

from django.contrib.auth.decorators import (
    login_required
)

# custom utils fuctions
from ..utils import (
    generate_random_string,
    generate_uuid
)


# form class
from ..forms import UserRegistrationForm

# User class
from ..models import User

## User Registration view function
def registrationView(request):
    """
    CREATE NEW USER WITH GIVEN EMAIL AND NAME
    GENERATE USER ID
    """
    context = {

    }

    # Post user sign up details if method is POST
    if request.POST:
        register_form = UserRegistrationForm(request.POST)   
        
        # check form field validity
        if register_form.is_valid():
            register_form.save()  # create and save user detail

            # get validated field data
            data = {
                'email': register_form.cleaned_data['email'],
                'raw_password': register_form.cleaned_data['password1']
            }

            # gets user using email
            user = User.objects.get(email=data['email'])
            # generate uuid
            user.user_id =  generate_uuid(use_host=True, use_id=True, use_time=True, rand=True)

            # set user type
            if user.profile_type == 'DR':   # if user signs up as a doctor
                user.is_doctor = True
            elif user.profile_type == 'PT': # if user signs up as a patient 
                user.is_patient = True
            # update and save the user detail
            user.save()

            # authenticate and log user in 
            user = authenticate(email=data['email'], password=data['raw_password'])
            login(request, user)
            return redirect('frontend:onboarding')   # redirect to user's dashboard

        # if the form or a field is not valid
        else:
            messages.error(request, "Please Correct Errors")
            context['register_form'] = register_form
    
    # if request method is GET
    else:
        register_form = UserRegistrationForm()
        context['register_form'] = register_form
    
    return render(request, 'authend/registration.html', context)


### THIS IS DEPRECATED CODE
@login_required()
def onboardingPath(request):
    user = request.user
    if user.is_patient:
        return redirect('patient_onboarding')
    elif user.is_doctor:
        return redirect('doctor_onboarding')