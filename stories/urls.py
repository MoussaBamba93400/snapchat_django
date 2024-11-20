from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.stories, name="stories"),
    path("add/", views.add_story, name="add_story"),
    path("story/<int:user_id>/", views.story_view, name="story_view"),
]
