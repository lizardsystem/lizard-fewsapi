# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import json
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from lizard_fewsapi.conf import settings  # Ensure it is loaded

FPL = ['filters', 'parameters', 'locations']


class FewsInstance(models.Model):
    """Pointer at REST API ('dac') of a FEWS instance."""
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Helpful textual identificator"),
        max_length=255,
        blank=True)
    url = models.URLField(
        help_text=_("Example: http://p-fews-ai-00-d3.external-nens.local:8081/FewsDacWebRS/api/v1.0"),
        max_length=255)
    # ^^^ URL to filter page, at the moment.

    class Meta:
        verbose_name = "FEWS instance"
        verbose_name_plural = "FEWS instances"
        ordering = ['url']

    def get_absolute_url(self):
        return reverse('fewsapi.fews_instance', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name or self.url

    @cached_property
    def download_urls(self):
        base_url = self.url.rstrip('/') + '/fews_sources/'
        return {key: base_url + key for key in FPL}

    @cached_property
    def cache_dir(self):
        base_dir = settings.LIZARD_FEWSAPI_CACHE_DIR
        return os.path.join(base_dir, str(self.id))

    @cached_property
    def json_filenames(self):
        return {key: os.path.join(self.cache_dir, key + '.json') for key in FPL}

    @cached_property
    def filters(self):
        return json.load(open(self.json_filenames['filters']))

    @cached_property
    def parameters(self):
        return json.load(open(self.json_filenames['parameters']))

    @cached_property
    def locations(self):
        return json.load(open(self.json_filenames['locations']))
