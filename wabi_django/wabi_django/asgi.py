"""
ASGI config for wabi_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import wabi.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wabi_django.settings')

# no channels / socket method:
# application = get_asgi_application()

application = ProtocolTypeRouter(
    {'http': get_asgi_application(),
     'websocket': AuthMiddlewareStack(
        URLRouter(
            wabi.routing.websocket_urlpatterns
        )
    )
    }
)
