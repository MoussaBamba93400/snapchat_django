from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message
from users.models import User
from friendships.models import Friendship
from django.views import View



class MessageView(View):
 @login_required
 def chat_view(request, friend_id):
    current_user = request.user
    friend = get_object_or_404(User, id=friend_id)

    print(current_user, friend)
    is_friend = Friendship.objects.filter(
        (
            Q(sender_user=current_user, recever_user=friend)
            | Q(sender_user=friend, recever_user=current_user)
        ),
        approved=True,
    ).exists()

    print("is_friend", is_friend)
    if not is_friend:
        return redirect("user_list")

    # Fetch the messages to display
    messages = Message.objects.filter(
    (Q(sender_user=current_user, recever_user=friend) & Q(viewed=False)) |
    (Q(sender_user=friend, recever_user=current_user) & Q(viewed=False))
   )
 
    messages_to_display = list(messages.values("id", "content", "viewed", "sender_user", "created_at"))

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(
                sender_user=current_user, recever_user=friend, content=content
            )
        return redirect("chat_view", friend_id=friend.id)

    context = {
        "friend": friend,
        "messages": messages_to_display,
    }
    print("context", context)
    return render(request, "chat.html", context)


 # Only use this if you're not using {% csrf_token %}, otherwise remove it
 def mark_message_as_viewed(request, friend_id):
        current_user = request.user
        friend = get_object_or_404(User, id=friend_id)
        messages = Message.objects.filter(
            sender_user=friend, recever_user=current_user, viewed=False
        )
        messages.update(viewed=True)
        return redirect('stories')