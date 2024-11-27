from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import *
from django.views.generic import CreateView
from .forms import *


class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy ('home')



def editAccount(request, id):
    user = get_object_or_404(CustomUser, id=id)
    
    if request.user.id != id:
        return render(request, 'unauthorized_error.html')
    
    if request.method== "POST":
        form = CustomUserEditForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =  CustomUserEditForm(instance = user)
    return render(request, 'registration/edituser.html', {'form':form})



def profile(request, id):
    pass