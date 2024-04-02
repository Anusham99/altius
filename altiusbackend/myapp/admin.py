from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(InvoiceHeader)
admin.site.register(InvoiceItems)
admin.site.register(InvoiceBillSundry)