from django.urls import path
from . import views

urlpatterns = [
    path('friends/', views.user_list_view, name='friends'),
    path("add_friend/<int:user_id>/", views.add_friend, name="add_friend"),
    path("remove_friend/<int:user_id>/", views.remove_friend, name="remove_friend"),
    path("accept_friend_request/<int:friendship_id>/", views.accept_friend_request, name="accept_friend_request"),
    path("reject_friend_request/<int:friendship_id>/", views.reject_friend_request, name="reject_friend_request"),
]
