from django.shortcuts import render
from models import Transactions

# Create your views here.
def wallet(request):
	transactions_obj = Transactions.objects.all()
	return render(request, 'wallet/index.html', {'transactions': transactions_obj})