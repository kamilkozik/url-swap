# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from url_swap.apps.main.views import show_form, add_url, show_url

urlpatterns = [
    # TODO(KK): Provide a view for below url
    url(r'^$', view=show_form, name='show_form'),
    url(r'^url/', include([
        url(r'^add/', view=add_url, name='add'),
        url(r'^show/(?P<proxy_url>[a-z0-9]{10})', view=show_url, name='show')
    ], namespace='url'))
]
