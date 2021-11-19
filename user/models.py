from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    follow = models.ManyToManyField(User, blank=True, related_name='follow')
    follower = models.ManyToManyField(User, blank=True, related_name='follower')

    def __str__(self):
        return self.owner
