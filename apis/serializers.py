from django.db.models import fields
from rest_framework import serializers
from pagos_app import models

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'title',
            'description',
            'amount',
            'adress',
            'typePage',
            'date'
        )
        model = models.Pagos