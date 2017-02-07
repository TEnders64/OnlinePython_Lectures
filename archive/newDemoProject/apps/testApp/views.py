from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    try:
        request.session['count'] += 1
    except:
        request.session['count'] = 0

    context = {
        'count' : request.session['count']
    }
    return render(request, 'testApp/index.html', context)

def create(request):
    request.session['username'] = request.POST['name']
    print request.method
    print request.POST['name']
    return redirect('/')
