# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

# from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext as _
from lizard_ui.views import UiView

from lizard_fewsapi import models


class FewsInstancesView(UiView):
    """Shows list of FEWS instances."""
    template_name = 'lizard_fewsapi/fews_instances.html'
    page_title = _('FEWS instances')
    edit_link = '/admin/lizard_fewsapi/fewsinstance/'

    @cached_property
    def fews_instances(self):
        return models.FewsInstance.objects.all()


class FewsInstanceView(UiView):
    """Shows FEWS instance debug information."""
    template_name = 'lizard_fewsapi/fews_instance.html'
    page_title = _('FEWS instance')

    @property
    def edit_link(self):
        return '/admin/lizard_fewsapi/fewsinstance/%s/' % self.kwargs['pk']

    @cached_property
    def fews_instance(self):
        return models.FewsInstance.objects.get(pk=self.kwargs['pk'])
