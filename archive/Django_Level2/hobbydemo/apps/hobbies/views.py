from django.shortcuts import render, redirect
from models import Hobby
# Create your views here.
def index(request):
    return render(request, 'hobbies/index.html')

def create(request):
    if request.method == 'POST':
        result = Hobby.objects.validate(name=request.POST['name'], description=request.POST['description'])
        if result[0]:
            return redirect('/all')
        else:
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect('/')

def all(request):
    hobbies = Hobby.objects.all()
    context = {'hobbies': hobbies}
    return render(request, 'hobbies/all.html', context)

def edit(request, hobby_id):
    h = Hobby.objects.get(id=hobby_id)
    print h.name
    context = {'hobby': h}
    return render(request, 'hobbies/edit.html', context)
#grab specific column from the hobbies dictionary list

def oneHobby(request, hobby_id):
    if request.method == "POST":
        #do updated stuff to hobby and redirect
        h = Hobby.objects.get(id=hobby_id)
        h.name = request.POST['name']
        h.description = request.POST['description'] #validate in future
        h.save()
        return redirect('/all')
    else:#it's a get
        #do some show stuff render template
        h = Hobby.objects.get(id=hobby_id)
        context = {'hobby': h}
        return render(request, 'hobbies/show.html', context)

def delete(request, hobby_id):
    h = Hobby.objects.get(id=hobby_id).delete()
    return redirect('/all')
