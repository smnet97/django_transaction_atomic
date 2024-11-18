import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "notifications"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

        await self.send(text_data=json.dumps({
            'message': "test notification 0"
        }))
        await self.send(text_data=json.dumps({
            'message': "test notification 1"
        }))
        await self.send(text_data=json.dumps({
            'message': "test notification 2"
        }))
        await self.send(text_data=json.dumps({
            'message': "test notification 3"
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    def receive(self, text_data):
        pass

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'message': "test notification"
        }))