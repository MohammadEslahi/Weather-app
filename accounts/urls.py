from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', CustomUserCreationView.as_view(), name='registration'),
]