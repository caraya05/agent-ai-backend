
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets  # pylint:disable=W0611

from configurations.helpers.utils_permissions import ActionBasedPermission
from companies.models.company import Company
from companies.serializers.company_serializer import CompanySerializer, \
    CompanyListSerializer, CompanyCreateSerializer


class CompanyViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901 C0112
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    action_permissions = {
        IsAuthenticated: ['create', 'update', 'partial_update',
                          "get_data_company", 'list', 'retrieve',
                          "get_data_general", "get_all_data_company",
                          "export_data_xlx", "get_users_access"],
        AllowAny: ['option', 'change_password', 'recovery_password']
    }
    permission_classes = (ActionBasedPermission,)
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['created_at', 'created_by']
    filter_fields = {
        'username': ['exact', ],
        'id': ['exact', ],
    }

    validate_owner_company = True

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CompanyCreateSerializer
        if self.action == 'retrieve':
            return self.serializer_class
        return CompanyListSerializer


EXAMPLE = (' ** { '
           '"id": "string", '
           '"name_company": "string", '
           '"person_in_charge": "string", '
           '"email": "string", '
           '"phone": "string", '
           '"address": "string", '
           '"nit": "string", '
           '"city": "UUID", '
           '"sector": "UUID", '
           '"size": "str", '
           '"image": "str", '
           '"password": "str", '
           '"company_type": "str", '
           '"activity_economic": "UUID", '
           ' } **')

CompanyViewSet.__doc__ = """
list:
   {LIST}
create:
    {CREATE}
retrieve:
   {RETRIEVE} 
update:
    {UPDATE}
partial_update:
    {PARTIAL_UPDATE}
destroy:
    {DESTROY}
""".format(
    LIST=_("List of all Persons registered in the system."),
    CREATE=_("Create a Persons data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific Persons."),
    UPDATE=_("Update a Persons data.") + EXAMPLE,
    PARTIAL_UPDATE=_(
        "Partially update a Persons data.") + ' ** { "year_start": 18 } **',
    DESTROY=_("Destroy a Persons data."),
)
