# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from url_swap.apps.main.models import UrlSwap


class UrlSwapAdmin(admin.ModelAdmin):
    list_display = ['proxy_url', 'origin_url']

admin.site.register(UrlSwap, UrlSwapAdmin)
