import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room_name = text_data_json['room_name']
        sender = text_data_json['sender']
        await self.create_message(room_name, sender, message)
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': text_data_json,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def create_message(self, room_name, sender, message):
        room = Room.objects.get(room_name=room_name)
        Message.objects.create(room=room, sender=sender, message=message)
