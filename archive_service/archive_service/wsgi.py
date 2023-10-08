"""
WSGI config for archive_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
# sys.path.append('/app')
# sys.path.append('/app/archive_service')

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..' )
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "archive_service.settings")

application = get_wsgi_application()
