from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=64, unique=True)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=32)

    # Risk & KYC Details
    kyc_status = models.CharField(max_length=16, choices=[
        ('PENDING', 'Pending'),
        ('VERIFIED', 'Verified'),
        ('ENHANCED', 'Enhanced'),
    ])
    kyc_last_updated = models.DateTimeField()
    risk_score = models.FloatField(default=0.0)
    suspicious_flags = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.user_id})"
