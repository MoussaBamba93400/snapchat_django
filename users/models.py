from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)  
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Si vous avez des champs supplémentaires, vous pouvez les ajouter ici

    def __str__(self):
        return self.username
