from django.db import models
from users.models import User

class Friendship(models.Model):
    id = models.BigAutoField(primary_key=True)
    approved = models.BooleanField(default=False)
    recever_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
    sender_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
