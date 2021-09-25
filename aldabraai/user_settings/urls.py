from django.urls import path

from user_settings.views import settings_view

app_name = 'settings'

urlpatterns = [
    path('', settings_view, name='setting-view')
]
