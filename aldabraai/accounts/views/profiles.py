from django import views

# django classbased views classes
from django.views.generic import (
    TemplateView,
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

# django functions
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.utils.text import (
    slugify
)

# auth and permission classes
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin
)

# models
from accounts.models import (
    Patient,
    Doctor
)

# forms
from frontend.forms.accounts import (
    PatientCreationForm
)

# PATIENT PROFILE VIEWS #


class PatientDetailView():
    pass

# PATIENT PROFILE CREATION VIEW
class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = 'accounts/createpatient.html'
    success_url = '/dashboard/'

    def form_valid(self, form):
        user = self.request.user

        form.instance.owner = user
        form.instance.slug = slugify(user.full_name)
        return super().form_valid(form)

# PATIENT PROFILE EDITION VIEW
class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = '/accounts/patientupdate_form.html'
    success_url = '/dashboard/'

    def get_object(self):   # GET USER PATIENT ACCOUNT
        user = self.request.user
        slug = self.kwargs['slug']  # USE SLUG FROM URL(USER)
        obj = get_object_or_404(Patient, slug=slug, owner=user)
        return obj


class PatientDeleteView():
    pass


# DOCTOR PROFILE VIEWS #
