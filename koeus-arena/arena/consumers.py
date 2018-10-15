# arena/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ArenaConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.arena_name = self.scope['url_route']['kwargs']['arena_name']
        self.arena_group_name = 'arena_%s' % self.arena_name



        # Join arena group
        await self.channel_layer.group_add(
            self.arena_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        # Leave arena group
        await self.channel_layer.group_discard(
            self.arena_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userName = text_data_json['userName']

        # Send message to arena group
        await self.channel_layer.group_send(
            self.arena_group_name,
            {
                'type': 'arena_message',
                'message': message,
                'userName': userName
            }
        )

    # Receive message from arena group
    async def arena_message(self, event):
        message = event['message']
        userName = event['userName']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'userName': userName
        }))
