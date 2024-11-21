from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:friend_id>/", views.chat_view, name="chat_view"),
    path('mark_message_as_viewed/<int:friend_id>', views.mark_message_as_viewed, name='mark_message_as_viewed'),
]
