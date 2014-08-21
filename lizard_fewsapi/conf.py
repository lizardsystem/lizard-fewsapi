# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import logging
import tempfile

from appconf import AppConf
from django.conf import settings

logger = logging.getLogger(__name__)


class MyAppConf(AppConf):
    CACHE_DIR = None

    def configure_cache_dir(self, value):
        if value is not None:
            return value
        tempdir  = tempfile.mkdtemp(prefix='fewsapi-')
        logger.warn(
            "LIZARD_FEWSAPI_CACHE_DIR is not set. Using a temp dir: %s",
            tempdir)
        return tempdir
