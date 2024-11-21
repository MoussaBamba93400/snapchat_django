from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form, "page": "register"})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            print(email, password)
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", "stories")
                return redirect(next_url)
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form, "page": "login"})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    user = request.user  # Récupère l'utilisateur connecté
    return render(request, 'profile.html', {'user': user})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Supprime le compte utilisateur
        messages.success(request, "Votre compte a été supprimé avec succès.")
        return redirect('register')  # Redirige vers la page d'accueil ou une autre page
    return render(request, 'delete_account.html')