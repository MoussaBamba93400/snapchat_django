from django.urls import path
from messaging.views import MessageView

urlpatterns = [
    path("chat/<int:friend_id>/", MessageView.chat_view, name="chat_view"),
    path('mark_message_as_viewed/<int:friend_id>', MessageView.mark_message_as_viewed, name='mark_message_as_viewed'),
]
