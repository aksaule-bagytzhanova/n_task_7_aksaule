from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('event_list')  # Укажите здесь URL вашей домашней страницы
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
