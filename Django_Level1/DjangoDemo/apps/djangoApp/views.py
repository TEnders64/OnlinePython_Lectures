from django.shortcuts import render
from .models import User
# Create your views here.
def show_users(request):
    if request.method == 'POST':
        #do POSTY things
        print request.POST
    else:
        #do GETTY things
        print "*" * 50
        print request.GET

    # all_users = User.objects.all() # SELECT * FROM users
    # print all_users
    request.session['user_id'] = 1
    print request.session['user_id']
    return render(request, 'djangoApp/index.html', {'user': 'Happy Gilmore'})
#
# def show_books(request):
#     all_books = Book.objects.all()

def login(request):
    if request.method == 'POST':
        result = User.objects.login(post=request.POST)
        if result[0]:
            request.session['user_id'] = result[1]['id']
        else:
            return redirect()
