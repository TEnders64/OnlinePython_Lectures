from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User, Language
# Create your views here.
def index(request):
    return render(request, 'user_languages/index.html')

def login(request):
    pass

def register(request):
    if request.method == "POST":
        result = User.objects.register(first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=request.POST['password'], c_password=request.POST['c_password'])
        if result[0]:
            request.session['user_id'] = result[1]
            return redirect(reverse('dashboard'))
        else:
            request.session['errors'] = result[1]
            return redirect(reverse('index'))

def dashboard(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    return render(request, 'user_languages/dashboard.html', context)
