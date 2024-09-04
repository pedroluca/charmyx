from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ProprietarioForm
from django.contrib.auth.models import Group

# Create your views here.
# uma transação só vai ocorrer no banco quando ocorre o commit, se não tenho o commit
def add(request):
    if request.method == 'POST':
        form = ProprietarioForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()

            
            prop_group, created = Group.objects.get_or_create(name='Proprietarios')  
            user.groups.add(prop_group) 
            return redirect("/pessoa/login")
    else:
        form = ProprietarioForm()
    return render(request, "registration/register.html", {"form":form})