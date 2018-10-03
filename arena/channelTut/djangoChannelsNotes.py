Django channels tutorial
=========================
python3 manage.py startapp chat
tutorial used: https://channels.readthedocs.io/en/latest/tutorial/part_2.html

add 'chat' to INSTALLED_APPS in mysite/settings.py

<project name>/routing.py
    # mysite/routing.py
    from channels.routing import ProtocolTypeRouter

    application = ProtocolTypeRouter({
        # (http->django views is added by default)
    })

add 'channels' to INSTALLED_APPS in settings.py
allso in <project name>/settings.py add:
    ASGI_APPLICATION = '<project name>.routing.application'


create consumers.py in <project name>/chat folder containing
    # chat/consumers.py
    from channels.generic.websocket import WebsocketConsumer
    import json

    class ChatConsumer(WebsocketConsumer):
        def connect(self):
            self.accept()

        def disconnect(self, close_code):
            pass

        def receive(self, text_data):
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            self.send(text_data=json.dumps({
                'message': message
            }))

create <project name>/chat/routing.py
    # chat/routing.py
    from django.conf.urls import url

    from . import consumers

    websocket_urlpatterns = [
        url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    ]

in <project name>/routing.py:
    # mysite/routing.py
    from channels.auth import AuthMiddlewareStack
    from channels.routing import ProtocolTypeRouter, URLRouter
    import chat.routing

    application = ProtocolTypeRouter({
        # (http->django views is added by default)
        'websocket': AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        ),
    })

Enable a channel layer
using redis
$ docker run -p 6379:6379 -d redis:2.8
$ pip3 install channels_redis

configure channel layers
under in settings.py ASGI_APPLICATION:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [('127.0.0.1', 6379)],
            },
        },
    }

update chat/consumers.py with: ## see tutorial 3 for async version
    # chat/consumers.py
    from asgiref.sync import async_to_sync
    from channels.generic.websocket import WebsocketConsumer
    import json

    class ChatConsumer(WebsocketConsumer):
        def connect(self):
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'chat_%s' % self.room_name

            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )

            self.accept()

        def disconnect(self, close_code):
            # Leave room group
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
            )

        # Receive message from WebSocket
        def receive(self, text_data):
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

        # Receive message from room group
        def chat_message(self, event):
            message = event['message']

            # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': message
            }))

Tutorial Part 3: Rewrite Chat Server as Asynchronous
    # chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

## dont forget redis is running off of docker

Tutorial Part 4: Automated Testing
using  Selenium

install chrome browser and chrome driver

pip3 install selenium

an obsene amount of code for testing
