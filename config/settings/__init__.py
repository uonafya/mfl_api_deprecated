from __future__ import absolute_import  # noqa
from .base import *  # noqa

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app  # noqa
