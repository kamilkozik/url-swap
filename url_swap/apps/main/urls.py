# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from url_swap.apps.main.views import show_form, add_url, show_url, redirect_to_origin

urlpatterns = [
    url(r'^$', view=show_form, name='show_form'),
    url(r'^(?P<proxy_url>[a-z0-9]{10})/', view=redirect_to_origin, name='redirect'),
    url(r'^url/', include([
        url(r'^add/', view=add_url, name='add'),
        url(r'^show/(?P<proxy_url>[a-z0-9]{10})', view=show_url, name='show')
    ], namespace='url'))
]
