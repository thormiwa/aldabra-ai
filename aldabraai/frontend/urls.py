from django.urls import (
    path,
    include
)

# Frontend default Views
from .views import (
    home,
    onboarding,
)

app_name = 'frontend app'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include("accounts.urls"), name='accounts'),
    path('dashboard/', include("dashboard.urls"), name='dashboard'),
    path('onboarding/', onboarding, name='onboarding'),
    path('settings/', include("user_settings.urls"), name='settings'),
    #path('patient/', include),
]
