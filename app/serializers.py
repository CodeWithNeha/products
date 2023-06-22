from rest_framework import serializers
from .models import *
class ProductSel(serializers.ModelSerializer):
    class Meta:
        model = ProductsDetails
        fields = ('__all__')