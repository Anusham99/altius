from rest_framework import serializers
from .models import *

class InvoiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceHeader
        fields = "__all__"

class InvoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItems
        fields = "__all__"

class InvoiceBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceBillSundry
        fields = "__all__"