from rest_framework.pagination import LimitOffsetPagination
from django.conf import settings


class CustomPagination(LimitOffsetPagination):
    default_limit = settings.DEFAULT_PAGINATION_LIMIT
    max_limit = settings.DEFAULT_PAGINATION_LIMIT
