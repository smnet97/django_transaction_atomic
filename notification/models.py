from django.db import models
from django.utils import timezone

class NotificationModel(models.Model):
    message = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

