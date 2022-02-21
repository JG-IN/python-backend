import os
from django.shortcuts import HttpResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PythonApiServer.settings")
import django
django.setup()

import channels.layers
async def test():
    group_name = 'group_a'
    channel_layer = channels.layers.get_channel_layer()
    await channel_layer.group_send(
         group_name,
        {
            'type': 'chat_message',
            'message': 'start'
        }
    )

import asyncio
asyncio.run(test())
