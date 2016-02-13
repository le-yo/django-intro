from rest_framework import viewsets
from models import Transactions
from api_serializers import TransactionsSerr

class TransactionsResource(viewsets.ModelViewSet):
    """mvutie waya"""
    serializer_class = TransactionsSerr
    queryset= Transactions.objects.all()
