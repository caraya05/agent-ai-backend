import random
import string

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from companies.managers.company_manager import CompanyManager


class Company(AbstractUser):
    model_name = "company"

    person_in_charge: str = models.CharField(_("Person in charge"), default="", max_length=256, null=True, blank=True)

    id_person_in_charge: str = models.CharField(_("Id person in charge"), default="", max_length=256, null=True,
                                                blank=True)
    name_company: str = models.CharField(_("name_company"), max_length=256, blank=True,
                                         null=True, default="")
    phone: str = models.CharField(_("phone"), max_length=16, blank=True,
                                  null=True, default="")
    address: str = models.CharField(_('Address'), max_length=500, blank=True,
                                    null=True)
    nit: str = models.CharField(_('Nit'), max_length=14, blank=True,
                                null=True)
    dv: str = models.CharField(_('DV'), max_length=1, blank=True,
                               null=True)
    rut: str = models.CharField(_('Rut'), max_length=14, blank=True,
                                null=True)
    contributory_regime: str = models.CharField(_('Contributory regime'), max_length=256, blank=True,
                                                null=True)
    is_responsible_for_iva: bool = models.BooleanField(_('Is responsible for iva'), default=False)

    city: str = models.CharField(_('City'), max_length=256, blank=True,
                                 null=True)

    department: str = models.CharField(_('Department'), max_length=256, blank=True,
                                       null=True)
    info_bank: str = models.CharField(_('Info bank'), max_length=256, blank=True,
                                      null=True)
    activity_economic: str = models.CharField(_('Economic activity'), max_length=256, blank=True,
                                              null=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    objects = CompanyManager()

    @staticmethod
    def id_generator() -> str:
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(25))

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return f'{self.name_company}'
