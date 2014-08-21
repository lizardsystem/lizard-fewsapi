# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import json
import logging
import os
from pprint import pprint

from django.core.management.base import BaseCommand

from lizard_fewsapi import collect
from lizard_fewsapi import models
from lizard_fewsapi.conf import settings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = ""
    help = "Download the filters/params/etc from the FEWS 'dac' API."

    def handle(self, *args, **options):
        base_dir = settings.LIZARD_FEWSAPI_CACHE_DIR
        for fews_instance in models.FewsInstance.objects.all():
            logger.debug("Downloading for %s", fews_instance)
            instance_dir = os.path.join(base_dir, str(fews_instance.id))
            if not os.path.exists(instance_dir):
                os.mkdir(instance_dir)
            filters_filename = os.path.join(instance_dir, 'filters.json')
            json.dump(collect.collect_filters(fews_instance.filters_url()),
                      open(filters_filename, 'w'),
                      indent=4)
            logger.info("Wrote %s", filters_filename)
