from __future__ import unicode_literals
import uuid
from django.db import models
from django.db.models import Sum

# Create your models here.


class Transactions(models.Model):
	REASON_CHOICES = (
		('SUBSCRIPTION', 'Subscription'),
		('WITHDRAWAL', 'Withdrawal'),
	)
	deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	transaction_id = models.CharField(
	    max_length=70, default=uuid.uuid4, unique=True)
	reason = models.CharField(max_length=20, choices=REASON_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	def total_deposits(self):
		return Transactions.objects.aggregate(total_deposits=Sum('deposit')).get('total_deposits') or 0.0

	def total_deductions(self):
		return Transactions.objects.aggregate(total_deductions=Sum('deduction')).get('total_deductions') or 0.0

	def balance(self):
		return self.total_deposits() - self.total_deductions()


	def __unicode__(self):
		return self.transaction_id

	class Meta:
		ordering = ('-created_at', )
		verbose_name = 'Transaction'
		verbose_name_plural = 'Transaction'
