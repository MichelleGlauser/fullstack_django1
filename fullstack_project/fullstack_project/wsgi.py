"""
WSGI config for fullstack_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# coding=utf-8
from __future__ import unicode_literals
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fullstack_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
