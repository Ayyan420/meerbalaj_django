"""
WSGI config for meer_balaj_cv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meer_balaj_cv.settings')

application = get_wsgi_application()
application = WhiteNoise(application)