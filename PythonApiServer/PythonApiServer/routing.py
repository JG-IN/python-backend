from channels.routing import ProtocolTypeRouter, URLRouter
from hashtag import routing

application = ProtocolTypeRouter({
    # http -> django views is added by default
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})