from django.shortcuts import render
from .models import Story
from django.contrib.auth.decorators import login_required

@login_required
def stories(request):
    stories = Story.objects.all()
    return render(request, 'stories.html', {'stories': stories})
