from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend, ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            print('EmailBackend')
            User = get_user_model()  
            user = User.objects.get(email=username) 
            if user.check_password(password): 
                return user
        except User.DoesNotExist:
            return None
