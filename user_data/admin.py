from django.contrib import admin

from banks.models import BankAccount
# Register your models here.
from .models import BankAccountUser
admin.site.register(BankAccountUser)
