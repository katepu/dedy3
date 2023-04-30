import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dedy_progi.settings')

application = get_wsgi_application()
