import os
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save    

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar  = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio     = models.TextField(null=True, blank=True)
    link    = models.URLField(max_length=200, null=True, blank=True)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created'):
        Profile.objects.get_or_create(user=instance)
        print('Se acaba de crear un usuario y su perfil enlazado')

@receiver(pre_save, sender=Profile)
def delete_image_avatar(sender, instance, **kwargs):
    if not kwargs.get('created'):
        oldAvatar = Profile.objects.get(pk=instance.pk).avatar
        if oldAvatar and os.path.isfile(oldAvatar.path):
            os.remove(oldAvatar.path)
