from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.stories, name='stories'),
    path('add/', views.add_story, name='add_story'),
]