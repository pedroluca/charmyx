from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClienteForm
from django.contrib.auth.models import Group

# Create your views here.
# uma transação só vai ocorrer no banco quando ocorre o commit, se não tenho o commit
def add(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()

    else:
        form = ClienteForm()
    return render(request, "registration/register.html", {"form":form})