from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            User = get_user_model()  # Get the custom user model
            user = User.objects.get(email=email)  # Look up user by email
            if user.check_password(password):  # Check if password matches
                return user
        except User.DoesNotExist:
            return None
