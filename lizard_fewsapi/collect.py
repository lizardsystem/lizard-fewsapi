# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import logging

import requests

logger = logging.getLogger(__name__)


def collect_filters(url):
    """Return filters from FEWS, cleaned and ready for storing as json."""
    from_fews = _download(url)
    result = []
    for filter_dict in from_fews:
        result.append(_process_filter_dict(filter_dict))
    return result


def collect_parameters(url):
    from_fews = _download(url)
    # TODO
    return from_fews


def collect_locations(url):
    from_fews = _download(url)
    # TODO
    return from_fews


def _download(url):
    r = requests.get(url)
    r.raise_for_status()  # Only raises an error when not succesful.
    return r.json()


def _process_filter_dict(filter_dict):
    # {'filter': {name, childfilters, etc}
    content = filter_dict['filter']
    name = content['name']
    description = content['description']
    if name == description:
        # Description is only interesting if it is different from the name.
        # Often it is the same, so we've got to filter it out.
        description = ''
    children = [_process_filter_dict(child_filter_dict)
                for child_filter_dict in content.get('childFilters', [])]
    result = {'id': content['id'],
              'name': name,
              'description': description,
              'children': children}
    return result
