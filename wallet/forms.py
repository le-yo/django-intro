from django import forms


class TransactionForm(forms.Form):
    deposit=forms.DecimalField(decimal_places=2, max_digits=11)
    deduction=forms.DecimalField(decimal_places=2, max_digits=11)
    reason=forms.CharField(max_length=45)
