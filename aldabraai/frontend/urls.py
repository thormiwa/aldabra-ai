from django.urls import (
    path,
    include
)

# Frontend Views
from .views import (
    home, 
    dashboard,
    onboarding,
    PatientCreateView,
    PatientUpdateView
)

app_name = 'frontend app'

patient_settings_urls = [
    path('profile/', PatientUpdateView.as_view(), name='patient_update_view')
]

doctor_settings_urls = [

]

settings_urls = [
    path('patient/', include(patient_urls)),
    path('doctor/', include(doctor_settings_urls))
]

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('onboarding/', onboarding, name='onboarding'),
    path('settings/', include(settings_urls)),
    path('patient/', include),
]
