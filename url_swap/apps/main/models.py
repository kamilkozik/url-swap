# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string

from django.db import models
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class UrlSwap(models.Model):
    origin_url = models.URLField(u'Url oryginalny', max_length=2048, blank=False, null=False)
    proxy_url = models.URLField(u'Proxy url', max_length=100, blank=False, null=False, db_index=True)

    def __str__(self):
        return self.origin_url

    @staticmethod
    def get_proxy_url(size):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))
