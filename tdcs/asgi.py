"""
ASGI config for tdcs project instead of the usual WSGI in order to embed a Bokeh Server in the Django project
"""
import os

import django

from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tdcs.settings')

django.setup()

application = get_default_application()
