# Generated by Django 4.2.3 on 2024-11-12 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_rename_customer_ne_invoice_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='invoice.invoice'),
        ),
    ]
