"""
 ROOT URL CONFIGURATION FILE
"""

from django.contrib import admin
from django.urls import (
    path,
    include
)

app_name = 'aldabra.ai'

## API(s) entry points
apis = [
    path('base/', include('base.urls')),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('hospitals/', include('hospitals.urls', namespace='hospitals')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('auth/', include('auths.urls')),
]

urlpatterns = [
    # FRONTEND APP --> DONT PLAY WITH THIS OR WE LOSE OUR NICE DISPLAY 
    path('', include('frontend.urls', namespace='frontend')),
    # API ENTRY version one --> DONT PLAY WITH THIS OR WE LOSE DATA
    path('api/v1/', include(apis)),
    path('admin/', admin.site.urls),
    path('auth/', include('auths.urls'))
]
