from django.urls import path
from .views import StoryView


urlpatterns = [
    path("list/", StoryView.stories, name="stories"),
    path("add/", StoryView.add_story, name="add_story"),
    path("story/<int:user_id>/", StoryView.story_view, name="story_view"),
]
