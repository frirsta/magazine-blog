from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, created, instance):
    if created:
        Profile.objects.create(user=instance)
