from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from loducode_utils.admin import AuditAdmin
from income_expenses.models.purchase_invoice_collection_account import PurchaseInvoiceCollectionAccount


class PurchaseInvoiceCollectionAccountResource(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceCollectionAccount
        # fields = "__all__"


@admin.register(PurchaseInvoiceCollectionAccount)
class PurchaseInvoiceCollectionAccountAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = PurchaseInvoiceCollectionAccountResource
    list_display = ("id", "invoice_number", "client_name", "issue_date", "due_date", "payment_status")
    list_display_links = ("id", "invoice_number", "client_name")
    search_fields = ("invoice_number", "client_name")
    list_filter = ("payment_status", "issue_date", "due_date")
    ordering = ("issue_date", "due_date", "invoice_number")