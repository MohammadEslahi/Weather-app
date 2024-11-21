from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView
from .forms import *


class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy ('home')