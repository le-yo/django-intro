from django.shortcuts import render,redirect
from models import Transactions
from wallet.forms import TransactionForm

# Create your views here.
def wallet(request):
	transactions_obj = Transactions.objects.all()
	return render(request, 'wallet/index.html', {'transactions': transactions_obj})

# Create your views here.
def addtransaction(request):
	if request.method == 'GET':
		form = TransactionForm


	if request.method == 'POST':
		form = TransactionForm(request.POST)
		if form.is_valid():
			deduction=form.cleaned_data['deduction']
			reason=form.cleaned_data['reason']
			deposit=form.cleaned_data['deposit']

			transaction = Transactions.objects.create(
			deduction=deduction,
			deposit=deposit,
			reason = reason
			)

			return redirect('/wallet')
	return render(request, 'wallet/create.html', {'form': form})
