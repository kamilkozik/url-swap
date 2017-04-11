from django import forms


class UrlSwapForm(forms.Form):
    original_url = forms.URLInput()
