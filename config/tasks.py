from celery import shared_task
from django.core.mail import send_mail

from config import settings
from notification.models import NotificationModel

@shared_task
def sent_notification(notification_id: int):
    try:
        notification = NotificationModel.objects.get(sent=False, id=notification_id)
        if notification:
            notification.sent = True
            notification.save()
            return "Ok"
    except NotificationModel.DoesNotExist:
        return "Error"




@shared_task
def send_mail_task(subject: str, message: str, recipient_list: list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
    )
    print("Xabar yuborildi !")


@shared_task
def my_task():
    for i in range(1_000_000):
        print(i)
