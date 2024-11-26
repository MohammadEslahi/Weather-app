from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('registration/', CustomUserCreationView.as_view(), name='registration'),
    path("edituser/<int:id>/", views.editAccount, name='edit_account'),
    path('', views.profile, name='profile'),
]