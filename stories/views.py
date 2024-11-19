from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Story
from .forms import StoryForm
from friendships.models import Friendship
from django.shortcuts import redirect

@login_required
def stories(request):
    user = request.user

    friendships = Friendship.objects.filter(
        approved=True, sender_user=user
    ) | Friendship.objects.filter(
        approved=True, recever_user=user
    )
    
    friend_ids = set()
    for friendship in friendships:
        if friendship.sender_user == user:
            friend_ids.add(friendship.recever_user_id)
        else:
            friend_ids.add(friendship.sender_user_id)
    
    stories = Story.objects.filter(user_id__in=friend_ids).order_by('-created_at')

    message = "Aucune story publiée par vos amis pour le moment." if not stories.exists() else None

    return render(request, 'stories.html', {'stories': stories, 'message': message, 'page': 'stories'})



@login_required
def add_story(request):
    if request.method == 'POST' and request.FILES:
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            # Assurez-vous d'associer l'utilisateur connecté à la story
            story = form.save(commit=False)  # Ne sauvegarde pas encore
            story.user = request.user  # Associe l'utilisateur connecté à la story
            story.save()  # Sauvegarde la story avec l'utilisateur associé
            return redirect('stories')  # Redirection après ajout
    else:
        form = StoryForm()
    return render(request, 'add_story.html', {'form': form})