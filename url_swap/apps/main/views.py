# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.response import TemplateResponse

from url_swap.apps.main.forms import UrlSwapForm


def show_form(request):
    context = {'form': UrlSwapForm}
    return TemplateResponse(request, template='main/show_form.html', context=context)
