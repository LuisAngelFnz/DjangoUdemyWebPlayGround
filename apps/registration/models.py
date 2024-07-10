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
    
    class Meta:
        ordering = ('user__username',)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created'):
        Profile.objects.get_or_create(user=instance)
        print('Se acaba de crear un usuario y su perfil enlazado')

@receiver(pre_save, sender=Profile)
def delete_image_avatar(sender, instance, **kwargs):
    if kwargs.get('created'): return 
    
    oldProfile = Profile.objects.filter(pk=instance.pk)
    if not oldProfile: return

    oldProfile = oldProfile.get()
    if instance.avatar and oldProfile.avatar:
        if instance.avatar.path == oldProfile.avatar.path:
            return
    if oldProfile.avatar and os.path.isfile(oldProfile.avatar.path):
        os.remove(oldProfile.avatar.path)
