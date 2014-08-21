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
        for fews_instance in models.FewsInstance.objects.all():
            logger.debug("Downloading for %s", fews_instance)
            if not os.path.exists(fews_instance.cache_dir):
                os.mkdir(fews_instance.cache_dir)
            for kind in models.FPL:  # Filters, parameters, locations
                filename = fews_instance.json_filenames[kind]
                url = fews_instance.download_urls[kind]
                collection_function = getattr(collect, 'collect_' + kind)
                json.dump(collection_function(url),
                          open(filename, 'w'),
                          indent=4)
                logger.info("Wrote %s", filename)
