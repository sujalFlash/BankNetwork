from django.db import models
from user_data.models import UserProfile
from banks.models import BankAccount

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('PAYMENT', 'Payment'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('DEPOSIT', 'Deposit'),
        ('TRANSFER', 'Transfer'),
    ]

    STATUS_CHOICES = [
        ('COMPLETED', 'Completed'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
    ]

    transaction_id = models.CharField(max_length=64, unique=True)
    sender = models.ForeignKey(UserProfile, related_name='sent_transactions', on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(UserProfile, related_name='received_transactions', on_delete=models.SET_NULL, null=True)
    sender_account = models.ForeignKey(BankAccount, related_name='sent_transactions', on_delete=models.SET_NULL, null=True)
    receiver_account = models.ForeignKey(BankAccount, related_name='received_transactions', on_delete=models.SET_NULL, null=True)
    bank_id = models.IntegerField()
    transaction_type = models.CharField(max_length=16, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    initiated_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    is_flagged = models.BooleanField(default=False)
    flagged_reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['is_flagged', 'amount']),
        ]
        ordering = ['-initiated_at']

    def __str__(self):
        return f"Transaction {self.transaction_id} ({self.amount} {self.currency})"

