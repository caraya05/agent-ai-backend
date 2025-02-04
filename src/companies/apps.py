from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CompanyConfig(AppConfig):
    name = 'companies'
    verbose_name = _("Companies")

    # def ready(self):
        # from .signals import create_history_initial_company   # pylint:disable= W0611, C0415
