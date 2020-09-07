from django.contrib.auth.models import AbstractUser
from django.db import models


class TwitterUser(AbstractUser):
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name='twitteruser_following',
        blank=True,
    )
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name='twitteruser_followers',
        blank=True,
    )
