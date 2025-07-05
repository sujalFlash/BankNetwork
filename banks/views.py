from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpReponse("<h1>Welcome to the Bank Network Management System</h1>")
