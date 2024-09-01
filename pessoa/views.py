from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProprietarioForm
from django.contrib.auth.models import Group

# Create your views here.
# uma transação só vai ocorrer no banco quando ocorre o commit, se não tenho o commit
def index(request):
    print('merda')