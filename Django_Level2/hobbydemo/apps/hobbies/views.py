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

def edit(request, hobby_id):
    h = Hobby.hobbyMgr.get(id=hobby_id)
    context = {'hobby': h}
    return render(request, 'hobbies/edit.html', context)

def oneHobby(request, hobby_id):
    if request.method == "POST":
        #do some UPDATE stuff
        h = Hobby.hobbyMgr.get(id=hobby_id)
        h.name = request.POST['name']
        h.description = request.POST['description']
        h.save()
        return redirect('/all')

    else: # it's a GET
        #do some SHOW stuff
        h = Hobby.hobbyMgr.get(id=hobby_id)
        context = {'hobby': h}
        return render(request, 'hobbies/show.html', context)

def delete(request, hobby_id):
    Hobby.hobbyMgr.get(id=hobby_id).delete()
    return redirect('/all')
