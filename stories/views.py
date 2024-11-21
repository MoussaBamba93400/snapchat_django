from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StorieView
from .models import Story
from .forms import StoryForm
from friendships.models import Friendship
from django.shortcuts import redirect
from django.views import View


class StoryView(View):
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
    
    latest_stories = Story.objects.filter(user_id__in=friend_ids).order_by('user_id', '-created_at')

    unique_stories = []
    seen_users = set()
    for story in latest_stories:
        if story.user.id not in seen_users:
            unique_stories.append(story)
            seen_users.add(story.user.id)
    
    message = "Aucune story publiée par vos amis pour le moment." if not unique_stories else None

    return render(request, 'stories.html', {'stories': unique_stories, 'message': message, 'page': 'stories'})



 @login_required
 def add_story(request):
    if request.method == 'POST' and request.FILES:
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            
            story = form.save(commit=False) 
            story.user = request.user  
            story.save() 
            return redirect('stories') 
    else:
        form = StoryForm()
    return render(request, 'add_story.html', {'form': form, 'page': 'add_story'})

 @login_required
 def story_view(request, user_id):
    try:
        stories = Story.objects.filter(user_id=user_id).order_by('-created_at')

        if not stories:
            stories = []
        else: 
            story_views = []
            for story in stories:
                print('story',story.id)
                story_views.append(StorieView(storie=story, viewer=request.user))
            StorieView.objects.bulk_create(story_views)    
    except Story.DoesNotExist:
        raise Http404("No stories found for this user")

    return render(request, 'story.html', {'stories': stories, 'page': 'story'})