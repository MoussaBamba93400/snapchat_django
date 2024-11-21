from django.urls import path
from .views import UserView

urlpatterns = [
   path('register/', UserView.register, name='register'),
   path('login/', UserView.login_view, name='login'),
   path('logout/', UserView.logout_view, name='logout'),
   path('profile/', UserView.profile_view, name='profile'),
   path('delete_account/', UserView.delete_account, name='delete_account'),
]
