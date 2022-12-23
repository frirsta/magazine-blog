from django.apps import AppConfig


class MagazineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'magazine'

    def ready(self):
        from . import signals
