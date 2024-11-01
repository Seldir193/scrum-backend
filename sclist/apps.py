




        
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class SclistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sclist'

    def ready(self):
        # Import to avoid side effects in module loading
        from .guest_utils import initialize_guest_user
        post_migrate.connect(initialize_guest_user, sender=self)
