"""User patterns for users"""

from django.urls import path, include

app_name = 'users'

urlspatterns = [
    path('', include('django.contrib.auth.urls'))
]