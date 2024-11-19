from django.contrib.auth import authenticate, login as django_login  # Renommé pour éviter le conflit
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm

# Vue d'enregistrement
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('login')  # Redirection vers la page de login
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form, 'page': 'register'})

# Vue de connexion
def login_view(request):  # Renommé pour éviter le conflit avec la méthode login de Django
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                next_url = request.GET.get('next', 'stories')  # Get the next URL or default to 'stories'
                return redirect(next_url)
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'page': 'login'})
