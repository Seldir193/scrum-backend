# guest_utils.py
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

def initialize_guest_user(**kwargs):
    """Creates a guest user and their authentication token if they don't already exist."""
    CustomUser = get_user_model()
    guest_user, created = CustomUser.objects.get_or_create(username="guest")
    if created:
        guest_user.set_password("guestpassword")
        guest_user.is_staff = False
        guest_user.save()
    
    # Token für Gastbenutzer erstellen
    Token.objects.get_or_create(user=guest_user)
