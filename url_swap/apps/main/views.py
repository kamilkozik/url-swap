# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse

from url_swap.apps.main.forms import UrlSwapForm
from url_swap.apps.main.models import UrlSwap


def show_form(request):
    return render(request, template_name='main/show_form.html', context={'form': UrlSwapForm()})


def add_url(request):
    if request.method == "POST":
        form = UrlSwapForm(request.POST)
        if form.is_valid():
            # create object and redirect to show_shortened_url view
            origin_url = form.cleaned_data['origin_url']
            try:
                url_swap = UrlSwap.objects.get(origin_url=origin_url)
            except UrlSwap.DoesNotExist:
                url_swap = UrlSwap.objects.create(origin_url=origin_url)
                while True:
                    proxy_url = UrlSwap.get_proxy_url(size=settings.PROXY_URL_SIZE)
                    if not UrlSwap.objects.filter(proxy_url=proxy_url).exists():
                        url_swap.proxy_url = proxy_url
                        url_swap.save()
                        break
            return redirect(reverse('main:url:show', kwargs={'proxy_url': url_swap.proxy_url}))

    return redirect(reverse('main:show_form'))


def show_url(request, proxy_url):
    try:
        url_swap = UrlSwap.objects.get(proxy_url=proxy_url)
    except UrlSwap.DoesNotExist:
        return redirect(reverse('main:show_form'))

    # create proxy_url with domain and protocol
    protocol = 'https' if request.is_secure() else 'http'
    site = get_current_site(request)
    proxy_url = url_swap.proxy_url
    return render(request, template_name='main/show_url.html',
                  context={'proxy_url': protocol + u'://' + site.domain + "/" + proxy_url})


def redirect_to_origin(request, proxy_url):
    try:
        url_swap = UrlSwap.objects.get(proxy_url=proxy_url)
    except UrlSwap.DoesNotExist:
        return redirect(reverse('main:show_form'))
    return redirect(url_swap.origin_url)
