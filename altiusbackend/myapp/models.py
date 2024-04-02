from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError
import uuid
from datetime import date


class InvoiceHeader(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    date = models.DateField(default=date.today)
    invoice_number = models.IntegerField(unique=True)
    customer_name = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    gst = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        total_item_amount = self.items.aggregate(total=Sum('amount'))['total']
        total_bill_amount = self.bills.aggregate(total=Sum('amount'))['total'] 
        self.total_amount = total_item_amount + total_bill_amount
        # super(InvoiceHeader, self).save(*args, **kwargs)
        # self.save()
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super(InvoiceHeader, self).save(*args, **kwargs)

class InvoiceItems(models.Model):
    header = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE, related_name='items')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    item_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def clean(self):
        self.amount = self.quantity * self.price
        if self.quantity <= 0:
            raise ValidationError("quantity must be greater than zero")
        if self.price <= 0:
            raise ValidationError("price must be greater than zero")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class InvoiceBillSundry(models.Model):
    header = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE, related_name='bills')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    bill_sundry_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
