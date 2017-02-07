from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'loginreg/index.html')

def login(request):
    if request.method == "POST":
        result = User.userMgr.login(email=request.POST['email'], password=request.POST['password'])
        if result[0]:
            request.session['user'] = result[1].first_name
            return redirect(reverse('_success'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('_index'))
    else:
        messages.add_message(request, messages.INFO, 'Please Try Again')
        return redirect(reverse('_index'))

def register(request):
    if request.method == "POST":
        result = User.userMgr.register(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], c_password=request.POST['c_password'])
        if result[0]:
            request.session['user'] = result[1].first_name
            return redirect(reverse('_success'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('_index'))
    else:
        messages.add_message(request, messages.INFO, 'Please Try Again')
        return redirect(reverse('_index'))

def success(request):
    return render(request, 'loginreg/success.html')
