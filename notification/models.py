from django.db import models

from twitteruser.models import TwitterUser


class Notification(models.Model):
    user = models.OneToOneField(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='notification_user'
    )
    mentioned_by = models.OneToOneField(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='notification_mention'
    )
