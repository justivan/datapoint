from .base import *
from .base import env

import socket

DEBUG = True

SECRET_KEY = "arhJ9NylBcua6vMrpgYWX7htaxJlAglYOdw7E2DNwgZMzYXqdQT26dncBDQcZV1V"

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# django-debug-toolbar
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = ["127.0.0.1"] + [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
