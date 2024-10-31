from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

def create_token_for_user(user):
    """Creates and returns an authentication token for the given user."""
    token, created = Token.objects.get_or_create(user=user)
    return token.key

def generate_jwt_tokens(user):
    """Generates and returns a refresh and access token for the user."""
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token)

def authenticate_user(username, password):
    """Authenticates the user with the provided username and password."""
    return authenticate(username=username, password=password)
