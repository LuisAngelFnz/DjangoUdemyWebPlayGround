from django.db import models
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('created', )


class Thread(models.Model):

    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)


def messageChanged(sender, **kwargs):
    instance = kwargs.pop('instance',None)
    action   = kwargs.pop('action',None)
    pk_set   = kwargs.pop('pk_set',None)

    if action == 'pre_add':
        for msg_pk in list(pk_set):
            message = Message.objects.get(pk=msg_pk)
            if message.user not in instance.users.all():
                pk_set.remove(msg_pk)
m2m_changed.connect(messageChanged, sender=Thread.messages.through)