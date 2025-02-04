from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from loducode_utils.admin import AuditAdmin
from income_expenses.models.sales_invoice import SalesInvoice


class SalesInvoiceResource(resources.ModelResource):
    class Meta:
        model = SalesInvoice
        # fields = "__all__"


@admin.register(SalesInvoice)
class SalesInvoiceAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = SalesInvoiceResource
    list_display = (
    "id", "invoice_number", "client_name", "issue_date", "due_date", "amount_to_be_received", "payment_status")
    list_display_links = ("id", "invoice_number", "client_name")
    search_fields = ("invoice_number", "client_name")
    list_filter = ("payment_status", "issue_date", "due_date")
    ordering = ("issue_date", "due_date", "invoice_number")
