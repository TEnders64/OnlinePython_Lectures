from django.shortcuts import render
from models import User, Language
# Create your views here.
def index(request):
    return render(request, 'user_languages/index.html')

def login(request):
    pass

def register(request):
    if request.method == "POST":
        result = User.objects.register(first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=request.POST['password'], c_password=request.POST['c_password'])
        print result
    return redirect('/')
