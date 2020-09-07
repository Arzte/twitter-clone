from django.db import models

from twitteruser.models import TwitterUser


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
