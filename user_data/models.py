from django.db import models
from django.db.models import JSONField  # Works in Django 3.1+

class BankAccountUser(models.Model):
    CUSTOMER_TYPES = [
        ('INDIVIDUAL', 'Individual'),
        ('CORPORATE', 'Corporate'),
    ]
    KYC_STATUS = [
        ('PENDING', 'Pending'),
        ('VERIFIED', 'Verified'),
        ('ENHANCED', 'Enhanced'),
    ]

    user_id = models.CharField(max_length=64, unique=True)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    primary_address = models.TextField()
    secondary_address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=32)
    customer_type = models.CharField(max_length=16, choices=CUSTOMER_TYPES)
    kyc_status = models.CharField(max_length=16, choices=KYC_STATUS)
    kyc_last_updated = models.DateTimeField()
    overall_risk_score = models.FloatField(default=0.0)

    # ✅ Replacing ArrayField with JSONField (compatible with SQLite)
    recent_login_ips = JSONField(default=list, blank=True)
    suspicious_flags = JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def validate_kyc(self):
        pass

    def calculate_risk_score(self):
        pass

    def add_login_event(self, event):
        pass

    def flag_suspicious(self, reason: str):
        self.suspicious_flags.append(reason)
        self.save()
