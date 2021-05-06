from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateClientForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user


@unauthenticated_user
def registration(request):
    form = CreateClientForm()
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = user.username
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('homePage')
    context = {'form': form, 'footertitle': 'Регистрация',}
    return render(request, 'reg/registration.html', context)


@unauthenticated_user
def next(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return redirect('registration')
    context = {'footertitle': 'Вход',}
    return render(request, 'reg/next.html', context)


def Ryzhovlogout(request):
    logout(request)
    return redirect('next')
