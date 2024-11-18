from django.db import models
from users.models import User

class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    viewed = models.BooleanField(default=False)
    sender_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recever_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
