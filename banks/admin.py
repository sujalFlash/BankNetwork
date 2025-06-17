from django.contrib import admin
from .models import  *
# Register your models here.
admin.site.register(Banks)
admin.site.register(BankAccount)
admin.site.register(Stakeholder)
admin.site.register(BankingProfessional)
admin.site.register(RetailBank)
admin.site.register(CommercialBank)
admin.site.register(CentralBank)
admin.site.register(InvestmentBank)
admin.site.register(CreditUnion)
admin.site.site_header = "Secura Admin Panel"
admin.site.site_title = "Welcome to Secura administration"
admin.site.index_title = "Welcome to the Secura"