"""
WSGI config for adnanportfilo project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'adnanportfilo' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adnanportfilo.settings')

application = get_wsgi_application()

# CRITICAL FOR VERCEL: 
# Vercel's Python runtime looks for 'app' specifically.
app = application