from django.db import models

from tweet.models import Tweet
from twitteruser.models import TwitterUser


class Notification(models.Model):
    user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='notification_user'
    )
    mentioned_by = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='notification_mention'
    )
    tweet = models.OneToOneField(
        Tweet,
        on_delete=models.CASCADE
    )
