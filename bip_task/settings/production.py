from .base import *

DEBUG = False

ALLOWED_HOSTS = ["bip-task.azurewebsites.net"]  # production domain

SESSION_COOKIE_SECURE = True
CRSF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000  # one year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
