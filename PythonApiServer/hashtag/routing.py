from django.urls import re_path
from hashtag import consumer

websocket_urlpatterns = [
    re_path(r'ws/hashtag/(?P<room_name>\w+)/$', consumer.HashtagConsumer.as_asgi())
]