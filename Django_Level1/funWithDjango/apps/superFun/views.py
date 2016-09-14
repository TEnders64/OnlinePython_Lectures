from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'superFun/index.html')

def users(request):
    return render(request, 'superFun/users.html')
