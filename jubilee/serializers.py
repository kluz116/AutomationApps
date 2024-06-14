from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class AddTransactionSerializer(serializers.Serializer):
    serial_id = serializers.CharField(max_length=10)
    trx_branchid = serializers.CharField(max_length=10)

class CustomerSerializer(serializers.Serializer):
    account_id = serializers.CharField(max_length=15)
