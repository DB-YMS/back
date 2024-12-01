from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    transactions_id = serializers.IntegerField(required=False)
    time_stamp = serializers.IntegerField(required=False)
    Details = serializers.CharField(required=False)

    class Meta:
        model = Transaction
        fields = '__all__'