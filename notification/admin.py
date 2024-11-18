from django.contrib import admin
from .models import NotificationModel

@admin.register(NotificationModel)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'sent']
    list_display_links = ['message']
    readonly_fields = ['sent']
