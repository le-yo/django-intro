from django.shortcuts import render
from models import Transactions
from wallet.forms import TransactionForm

# Create your views here.
def wallet(request):
	transactions_obj = Transactions.objects.all()
	return render(request, 'wallet/index.html', {'transactions': transactions_obj})

# Create your views here.
def addtransaction(request):
	form = TransactionForm()
	return render(request, 'wallet/create.html', {'form': form})
