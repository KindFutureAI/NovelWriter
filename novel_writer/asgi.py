"""
ASGI config for novel_writer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novel_writer.settings")

# application = get_asgi_application()


# 为实现一个websocket服务，需要做以下几件事情：
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from novel_writer import routings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novel_writer.settings")

# 支持 http 和 WebSocket 请求
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 自动找 urls.py ， 找视图函数  --》 http
    "websocket": URLRouter(routings.websocket_urlpatterns),  # routing(urls)、 consumers(views)
})