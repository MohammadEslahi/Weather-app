from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.views.generic import CreateView
from .forms import *


class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy ('home')



def editAccount(request, id):
    user = get_object_or_404(CustomUser, id=id)
    form = CustomUserEditForm(request.POST, request.FILES, instance = user)
    
    if request.user.id != id:
        return render(request, 'unauthorized_error.html')
    
    if request.method== "POST":
        # logic for removing profile image
        if 'Delete profile image' in request.POST:
            user.profile_image = 'profile_image/default_profile_image.jpg'
            user.save()
            return redirect('edit_account', id)
        # logic for editing user account
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully edited!')
            return redirect('home')
    else:
        form =  CustomUserEditForm(instance = user)
    return render(request, 'registration/edituser.html', {'form':form})