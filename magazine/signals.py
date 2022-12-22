from django.db.models.signals import post_save
from .models import User, UserProfile


def create_profile(post_save, sender, created, instance):
    if created:
        Profile.objects.create(user=instance)
