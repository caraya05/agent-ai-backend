from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommonsConfig(AppConfig):
    name = 'configurations'
    verbose_name = _('Commons')
