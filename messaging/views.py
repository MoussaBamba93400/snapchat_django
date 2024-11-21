from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message
from users.models import User
from friendships.models import Friendship

@login_required
def chat_view(request, friend_id):
    """Affiche et gère la messagerie avec un ami."""
    current_user = request.user
    friend = get_object_or_404(User, id=friend_id)

    # Vérifier si l'utilisateur et le destinataire sont amis
    is_friend = Friendship.objects.filter(
        (Q(sender_user=current_user, recever_user=friend) | Q(sender_user=friend, recever_user=current_user)),
        approved=True
    ).exists()

    if not is_friend:
        return redirect("user_list")

    # Récupérer les messages entre les deux utilisateurs
    messages = Message.objects.filter(
        (Q(sender_user=current_user, recever_user=friend) & Q(viewed=False)) |
        (Q(sender_user=friend, recever_user=current_user) & Q(viewed=False))
    ).order_by("created_at")

    # Marquer les messages reçus comme vus
    messages.filter(sender_user=friend, recever_user=current_user).update(viewed=True)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(
                sender_user=current_user,
                recever_user=friend,
                content=content
            )
        return redirect("chat_view", friend_id=friend.id)

    context = {
        "friend": friend,
        "messages": messages,
    }
    return render(request, "chat.html", context)
