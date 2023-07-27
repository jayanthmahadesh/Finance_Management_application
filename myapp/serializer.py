from rest_framework import serializers
from .models import *

class expense_serializer(serializers.ModelSerializer):
    class Meta:
        model=expense
        fields ='__all__'