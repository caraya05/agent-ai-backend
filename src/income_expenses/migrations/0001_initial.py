# Generated by Django 3.0 on 2025-02-04 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('invoice_number', models.CharField(max_length=20, verbose_name='Invoice Number')),
                ('order_number', models.CharField(max_length=20, verbose_name='Order Number')),
                ('client_name', models.CharField(max_length=100, verbose_name='Client Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('amount_base', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Taxable Base')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IVA')),
                ('retefuente', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ReteFuente')),
                ('reteica', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ReteICA')),
                ('reteiva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ReteIVA')),
                ('amount_to_be_received', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount to be Received')),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Partial', 'Partial')], max_length=20, verbose_name='Payment Status')),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount Received')),
                ('self_retention', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Self Retention')),
                ('pay_date', models.DateField(blank=True, null=True, verbose_name='Pay Date')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoices', to=settings.AUTH_USER_MODEL, verbose_name='company')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salesinvoice_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salesinvoice_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseInvoiceCollectionAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('invoice_number', models.CharField(max_length=20, verbose_name='Invoice Number')),
                ('client_name', models.CharField(max_length=100, verbose_name='Supplier Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('amount_base', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Taxable Base')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IVA')),
                ('retefuente', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ReteFuente')),
                ('reteica', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ReteICA')),
                ('reteiva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ReteIVA')),
                ('amount_to_be_paid', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Partial', 'Partial')], max_length=20, verbose_name='Payment Status')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount Paid')),
                ('pay_date', models.DateField(blank=True, null=True, verbose_name='Pay Date')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchaseinvoicecollectionaccount_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchaseinvoicecollectionaccount_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
