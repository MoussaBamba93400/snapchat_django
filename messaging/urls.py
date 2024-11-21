from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:friend_id>/", views.chat_view, name="chat_view"),
]
