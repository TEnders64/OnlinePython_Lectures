from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'testApp/index.html')
