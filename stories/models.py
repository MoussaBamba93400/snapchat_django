from django.db import models
from users.models import User

class Story(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    content_image = models.ImageField(upload_to='stories/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StorieView(models.Model):
    id = models.BigAutoField(primary_key=True)
    viewer = models.ForeignKey(User, related_name='viewed_stories', on_delete=models.CASCADE)
    storie = models.ForeignKey(Story, related_name='views', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
