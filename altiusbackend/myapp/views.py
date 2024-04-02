from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class InvoiceView(viewsets.ModelViewSet):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer
    