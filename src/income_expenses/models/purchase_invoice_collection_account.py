from django.db import models
from loducode_utils.models import Audit
from django.utils.translation import gettext_lazy as _


class PurchaseInvoiceCollectionAccount(Audit):
    invoice_number = models.CharField(_('Invoice Number'), max_length=20)
    client_name = models.CharField(_('Supplier Name'), max_length=100)
    description = models.TextField(_('Description'))
    issue_date = models.DateField(_('Issue Date'))
    due_date = models.DateField(_('Due Date'))
    amount_base = models.DecimalField(_('Taxable Base'), max_digits=10, decimal_places=2)
    iva = models.DecimalField(_('IVA'), max_digits=10, decimal_places=2)
    retefuente = models.DecimalField(_('ReteFuente'), max_digits=10, decimal_places=2)
    reteica = models.DecimalField(_('ReteICA'), max_digits=10, decimal_places=2)
    reteiva = models.DecimalField(_('ReteIVA'), max_digits=10, decimal_places=2)
    amount_to_be_paid = models.DecimalField(_('Total Amount'), max_digits=10, decimal_places=2)
    payment_status = models.CharField(_('Payment Status'), max_length=20,
                                      choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Partial', 'Partial')], )
    amount_paid = models.DecimalField(_('Amount Paid'), max_digits=10, decimal_places=2)
    pay_date = models.DateField(_('Pay Date'), null=True, blank=True)

    def __str__(self):
        return f'{self.invoice_number} - {self.client_name}'
