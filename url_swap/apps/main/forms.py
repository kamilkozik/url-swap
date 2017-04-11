from django import forms


class UrlSwapForm(forms.Form):
    origin_url = forms.URLField(label='Adres url', required=True)
