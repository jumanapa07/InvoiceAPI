from rest_framework import serializers
from .models import *

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =InvoiceDetail
        fields=['id','description','quantity','price','line_total']
        read_only_fields = ['line_total']

class InvoiceSerializer(serializers.ModelSerializer):
    details=InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def create(self,validated_data):
        details_data=validated_data.pop('details')
        #invoice row created
        invoice= Invoice.objects.create(**validated_data)
        # each details of specific invoice are added to invoicedetail
        for data in details_data:
            InvoiceDetail.objects.create(invoice=invoice,**data)

        return invoice
    def update( self , instance , validated_data):
        details_data=validated_data.pop('details')
        #update each invoice model fields
        instance.invoice_number=validated_data.get('invoice_number',instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        # removed previous details and add updates ones
        instance.details.all().delete()
        for data in details_data:
            InvoiceDetail.objects.create(invoice=instance,**data)
        return instance
        
