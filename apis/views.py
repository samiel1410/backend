from django.shortcuts import render
from rest_framework import serializers, generics
from pagos_app import models
from .serializers import PagosSerializer

# Create your views here.

class ListPagos(generics.ListCreateAPIView):
    queryset = models.Pagos.objects.all()
    serializer_class = PagosSerializer

class DetailPagos(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pagos.objects.all()
    serializer_class = PagosSerializer