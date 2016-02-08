from rest_framework import serializers
from models import Transactions

class TransactionsSer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = (
            'id',
            'deposit',
            'deduction',
            'transaction_id',
            'reason',
            'created_at',
            'updated_at',
        )
        depth = 0