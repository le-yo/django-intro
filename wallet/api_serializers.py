from rest_framework import serializers
from models import Transactions

class TransactionsSerr(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        field = (
        'id',
        'deduction'
        'owner'
        )
        depth=1
