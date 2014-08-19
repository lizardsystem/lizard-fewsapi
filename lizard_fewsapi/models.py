# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

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
        help_text=_("URL of the FEWS instance's REST API"),
        max_length=255)

    class Meta:
        verbose_name = "FEWS instance"
        verbose_name_plural = "FEWS instances"
        ordering = ['url']

    def __unicode__(self):
        return self.name or self.url
