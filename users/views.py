from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('login')  # Redirection vers la page de login
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Vérification du mot de passe hashé

            if user is not None:
                login(request, user)  # Connexion de l'utilisateur
                return redirect('home')  # Page d'accueil après la connexion
            else:
                messages.error(request, 'Identifiants incorrects.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})