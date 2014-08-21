# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from lizard_fewsapi import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',
        views.FewsInstancesView.as_view(),
        name='fewsapi.fews_instances'),
    url(r'^fews-instance/(?P<pk>\d+)/$',
        views.FewsInstanceView.as_view(),
        name='fewsapi.fews_instance'),
    url(r'^ui/', include('lizard_ui.urls')),
    url(r'^admin/', include(admin.site.urls)),
    )
urlpatterns += debugmode_urlpatterns()
