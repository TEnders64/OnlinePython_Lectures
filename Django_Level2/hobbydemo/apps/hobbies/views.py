from django.shortcuts import render, redirect
from models import Hobby
# Create your views here.
def index(request):
    return render(request, 'hobbies/index.html')

def create(request):
    if request.method == 'POST':
        result = Hobby.hobbyMgr.validate(name=request.POST['name'], description=request.POST['description'])
        if result[0]:
            return redirect('/all')
        else:
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect('/')

def all(request):
    hobbies = Hobby.hobbyMgr.all()
    context = {'hobbies': hobbies}
    return render(request, 'hobbies/all.html', context)
