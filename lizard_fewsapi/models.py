# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


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

    def base_url(self):
        base = self.url.rstrip('/')
        return base + '/fews_sources/'

    def parameters_url(self):
        return self.base_url() + 'parameters'

    def filters_url(self):
        return self.base_url() + 'filters'

    def locations_url(self):
        return self.base_url() + 'locations'
