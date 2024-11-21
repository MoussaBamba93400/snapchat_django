from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User, Friendship

@login_required
def user_list_view(request):
    current_user = request.user

    # Récupérer tous les utilisateurs sauf l'utilisateur connecté
    users = User.objects.exclude(id=current_user.id)

    # Déterminer le statut d'amitié pour chaque utilisateur
    user_statuses = []
    for user in users:
        friendship = Friendship.objects.filter(
            (Q(sender_user=current_user, recever_user=user) | Q(sender_user=user, recever_user=current_user)),
            approved=True
        ).first()

        if friendship:
            status = "friend"
        else:
            pending_request = Friendship.objects.filter(
                (Q(sender_user=current_user, recever_user=user, approved=False) | Q(sender_user=user, recever_user=current_user, approved=False))
            ).exists()
            status = "pending" if pending_request else "not_friend"
        print(status, user)
        if status != "pending":
          user_statuses.append({
            "user": user,
            "status": status
          })

    # Récupérer les demandes d'amitié en attente
    pending_friend_requests = Friendship.objects.filter(recever_user=current_user, approved=False)

    context = {
        "user_statuses": user_statuses,
        "pending_friend_requests": pending_friend_requests,
        'page': 'friends'
    }

    return render(request, "friends.html", context)


@login_required
def add_friend(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    Friendship.objects.create(sender_user=request.user, recever_user=receiver)
    return redirect("friends")

@login_required
def remove_friend(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Friendship.objects.filter(
        Q(sender_user=request.user, recever_user=other_user) | 
        Q(sender_user=other_user, recever_user=request.user)
    ).delete()
    return redirect("friends")

@login_required
def accept_friend_request(request, friendship_id):
    """Accepter une demande d'amitié."""
    friendship = get_object_or_404(Friendship, id=friendship_id, recever_user=request.user)
    friendship.approved = True
    friendship.save()
    return redirect("friends")

@login_required
def reject_friend_request(request, friendship_id):
    """Refuser une demande d'amitié (supprimer la demande)."""
    friendship = get_object_or_404(Friendship, id=friendship_id, recever_user=request.user)
    friendship.delete()
    return redirect("friends")