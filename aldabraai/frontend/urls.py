from django.urls import path

from .views import (
    home,
    dashboard,
    onboarding
)

app_name = 'frontend'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('onboarding/', onboarding, name='onboarding')
]
