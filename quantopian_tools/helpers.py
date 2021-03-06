# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, unicode_literals

from requests.compat import urlencode

from quantopian_tools import settings


def build_url(*parts, **query):
    query = urlencode(query)
    return '{scheme}://{base}/{path}{query}'.format(scheme='https',
                                                    base=settings.QUANTOPIAN_HOST,
                                                    path='/'.join(p.lstrip('/') for p in parts),
                                                    query='?' + query if query else '')
