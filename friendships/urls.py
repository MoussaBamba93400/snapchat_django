from django.urls import path
from .views import FriendshipView

urlpatterns = [
    path('friends/', FriendshipView.user_list_view, name='friends'),
    path("add_friend/<int:user_id>/", FriendshipView.add_friend, name="add_friend"),
    path("remove_friend/<int:user_id>/", FriendshipView.remove_friend, name="remove_friend"),
    path("accept_friend_request/<int:friendship_id>/", FriendshipView.accept_friend_request, name="accept_friend_request"),
    path("reject_friend_request/<int:friendship_id>/", FriendshipView.reject_friend_request, name="reject_friend_request"),
]
