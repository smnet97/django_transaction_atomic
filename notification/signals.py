from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NotificationModel
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from uuid import uuid4


@receiver(post_save, sender=NotificationModel)
def create_notification(sender, created, instance, **kwargs):

    if created:
        clocked = ClockedSchedule.objects.create(
            clocked_time=instance.date,
        )
        PeriodicTask.objects.create(
            name=instance.message + " " + str(uuid4()),
            task="config.tasks.sent_notification",
            clocked=clocked,
            one_off=True,
            args=[instance.pk],
        )

