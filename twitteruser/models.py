from django.db import models

from authentication import AuthUser


class TwitterUser(models.Model):
    AuthUser = models.OneToOneField(AuthUser)
