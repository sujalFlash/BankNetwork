from django.shortcuts import render
from django.http import JsonResponse
from user_data.models import UserProfile
from banks.models import BankAccount
from django.utils.crypto import get_random_string
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_fake_transaction(request):
    users = list(UserProfile.objects.all())
    accounts = list(BankAccount.objects.select_related('user').all())

    if len(users) < 2 or len(accounts) < 2:
        return JsonResponse({"error": "Not enough users/accounts to generate transactions."}, status=400)

    sender = random.choice(users)
    receiver = random.choice([u for u in users if u.user_id != sender.user_id])

    sender_accounts = [a for a in accounts if a.user == sender]
    receiver_accounts = [a for a in accounts if a.user == receiver]

    if not sender_accounts or not receiver_accounts:
        return JsonResponse({"error": "Sender or Receiver has no accounts."}, status=400)

    sender_account = random.choice(sender_accounts)
    receiver_account = random.choice(receiver_accounts)

    amount = round(random.uniform(10, 10000), 2)
    transaction_data = {
        "transaction_id": get_random_string(12),
        "sender_id": sender.id,
        "reciever_id": receiver.id,
        "bank_id": sender_account.id,  # Using sender's bank account id
        "transaction_type": random.choice(["PAYMENT", "WITHDRAWAL", "DEPOSIT", "TRANSFER"]),
        "amount": amount,
        "currency": sender_account.currency,
        "sender_account": sender_account.account_id,
        "receiver_account": receiver_account.account_id,
        "status": random.choice(["COMPLETED", "PENDING", "FAILED", "CANCELLED"]),
        "initiated_at": fake.date_time_between(start_date='-30d', end_date='now').isoformat(),
        "completed_at": datetime.now().isoformat(),
        "is_flagged": random.choice(["true", "false"]),
        "flagged_reason": random.choice(["Suspicious Pattern", "High Amount", "Unusual Destination", None]),
    }

    return JsonResponse(transaction_data)
