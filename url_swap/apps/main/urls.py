# -*- coding: utf-8 -*-
from django.conf.urls import url

from url_swap.apps.main.views import show_form

urlpatterns = [
    # TODO(KK): Provide a view for below url
    url(r'^$', view=show_form, name='show_form')
]
