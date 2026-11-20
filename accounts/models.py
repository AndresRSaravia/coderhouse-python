from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Foto de perfil") no funciona pillow
    avatar = models.FileField(upload_to='avatars/', blank=True, null=True, verbose_name="Foto de perfil")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biografía")

    def __str__(self):
        return f"Perfil de {self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)