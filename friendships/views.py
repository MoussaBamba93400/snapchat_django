from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def friends(request):
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)  # Exclure l'utilisateur connecté
    friends = current_user.friends.all()  # Liste des amis de l'utilisateur connecté

    # Annoter chaque utilisateur pour indiquer s'il est un ami
    users_with_status = [
        {
            'user': user,
            'is_friend': user in friends
        }
        for user in users
    ]

    return render(request, 'friends.html', {'users': users_with_status, 'page': 'friends'})
