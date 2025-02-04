from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from loducode_utils.admin import AuditAdmin
from companies.models.company import Company


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
        # fields = "__all__"


@admin.register(Company)
class CompanyAdmin(UserAdmin, AuditAdmin, ImportExportModelAdmin):
    resource_class = CompanyResource

    list_display = (
        "id", "username", "name_company", "person_in_charge", "phone", "address",
        "nit", "city", "email",)
    list_display_links = (
        "id", "username", "name_company", "person_in_charge", "phone", "address",
        "nit", "city", 'email',)

    search_fields = ("person_in_charge", "username",)
    list_filter = ("name_company",)
    readonly_fields = ('token',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal information'), {
            'fields': ('name_company', 'person_in_charge', 'email', 'phone',
                       'address', 'nit', 'city', 'activity_economic', 'token',
                       )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important data'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'name_company', 'password1', 'password2',
                "person_in_charge", 'id_person_in_charge', 'phone', 'address', 'nit', 'dv', 'rut',
                'contributory_regime', 'is_responsible_for_iva', 'city', 'department', 'info_bank', 'activity_economic',
                "email",),
        }),
    )

    actions = ['make_permission_init', 'deactivate_notification', 'add_email', ]
