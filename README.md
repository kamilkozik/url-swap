### Installation guide

```
pip install -r requirements.txt
./manage.py migrate --settings=url_swap.settings.base
./manage.py runserver --settings=url_swap.settings.base
```

Provide mysql db credentials at `url_swap/settings/base.py` (user, pass, etc.)