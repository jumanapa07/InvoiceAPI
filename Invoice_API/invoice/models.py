from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoiceNum = models.CharField(max_length=30,unique=True)
    date=models.DateField()
    customerName=models.CharField(max_length=100)

    def __str__(self):
        return self.invoiceNum

class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self,*args,**kwargs):
        self.line_total=self.quantity* self.price
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.description} ({self.invoice.invoiceNum})"