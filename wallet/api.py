from rest_framework import viewsets
from rest_framework import filters

from models import Transactions
from serializers import TransactionsSer


class TransactionsViewSet(viewsets.ModelViewSet):
    """
    Transactions api resource
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSer
