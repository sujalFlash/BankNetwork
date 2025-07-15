from django.urls import path
from .views import generate_fake_transaction

urlpatterns = [
    path('generate_fake_transaction/', generate_fake_transaction, name='generate_fake_transaction'),
]
