from django.db import models
from django.db.models import JSONField
from user_data.models import *
from django.conf import settings
from django.db.models import Q,JSONField
class Banks(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=100)
    bank_headquarter = models.TextField()
    currency = models.CharField(max_length=10)
    bank_country = models.CharField(max_length=10)

    bank_choices = [
        ("COMMERCIAL", "commercial"),
        ("CENTRAL", "central"),
        ("INVESTMENT", "investment"),
        ("OTHER", "other"),
    ]

    swift_code = models.CharField(max_length=11, unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    regulatory_authority = models.CharField(max_length=10)
    bank_type = models.CharField(max_length=16, choices=bank_choices)
    branch_ids = JSONField(default=list, blank=True)  # ✅ FIXED

class BankAccount(models.Model):
    ACCOUNT_STATUS = [
        ('ACTIVE', 'Active'),
        ('FROZEN', 'Frozen'),
        ('CLOSED', 'Closed'),
    ]

    account_id = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(BankAccountUser, related_name='accounts', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=32)
    currency = models.CharField(max_length=3)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2)
    branch_id = models.CharField(max_length=64)
    status = models.CharField(max_length=16, choices=ACCOUNT_STATUS)
    opened_at = models.DateTimeField()
    closed_at = models.DateTimeField(blank=True, null=True)
    watchlist_indicators = JSONField(default=list, blank=True)  # ✅ FIXED

    def freeze_account(self):
        self.status = 'FROZEN'
        self.save()

    def get_recent_transactions(self):
        return self.transactions.order_by('-timestamp')[:50]

class BankingProfessional(models.Model):
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='banking_profile',
        limit_choices_to=Q(banking_profile_isnull=True)
    )
    ROLE_CHOICES = [
        ("ANALYST", "Analyst"),
        ("INVESTIGATOR", "Investigator"),
        ("COMPLIANCE", "Compliance Officer"),
        ("ADMIN", "Admin"),
        ("AUDITOR", "Auditor"),
        ("EXECUTIVE", "Executive"),
    ]
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("SUSPENDED", "Suspended"),
        ("DEACTIVATED", "Deactivated"),
    ]

    professional_id = models.CharField(max_length=64, unique=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=64)
    permissions = JSONField(default=dict)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="ACTIVE")
    auth_provider = models.CharField(max_length=32, default="Password")
    preferred_language = models.CharField(max_length=10, default="en-US")
    timezone = models.CharField(max_length=64, default="UTC")
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    mfa_enabled = models.BooleanField(default=True)
    security_clearance = models.CharField(max_length=16, default="Level1")
    access_regions = JSONField(default=list, blank=True)  # ✅ FIXED
    bank=models.ForeignKey(Banks, on_delete=models.CASCADE)
    
class CentralBank(Banks):
    monetary_policy_framework = models.TextField()
    reserve_requirement_ratio = models.DecimalField(max_digits=5, decimal_places=2)

class CommercialBank(Banks):
    ifsc_code = models.CharField(max_length=11)
    correspondent_swift_codes = JSONField(default=list, blank=True)  # ✅ FIXED

class InvestmentBank(Banks):
    underwriting_standards = models.TextField()
    trading_desk_ids = JSONField(default=list, blank=True)  # ✅ FIXED
    prime_brokerage_partners = JSONField(default=list, blank=True)  # ✅ FIXED

class RetailBank(Banks):
    branch_locations = JSONField(default=list, blank=True)  # ✅ FIXED
    atm_network_id = models.CharField(max_length=64)
    supported_card_networks = JSONField(default=list, blank=True)  # ✅ FIXED

class CreditUnion(Banks):
    registration_number = models.CharField(max_length=64)
    dividend_rate = models.DecimalField(max_digits=5, decimal_places=2)

class Stakeholder(models.Model):
    STAKEHOLDER_TYPES = [
        ('REGULATOR', 'Regulator'),
        ('AUDITOR', 'Auditor'),
        ('EXECUTIVE', 'Executive'),
        ('PARTNER_BANK', 'Partner Bank'),
    ]

    stakeholder_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=200)
    stakeholder_type = models.CharField(max_length=16, choices=STAKEHOLDER_TYPES)
    organization = models.CharField(max_length=200)
    contact_info = JSONField()  # ✅ Already fixed in earlier step
    areas_of_interest = JSONField(default=list, blank=True)  # ✅ FIXED
    regulated_banks = models.ManyToManyField('CommercialBank', related_name='regulators', blank=True)
