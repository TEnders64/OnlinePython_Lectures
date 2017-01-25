from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User, Language
# Create your views here.
def index(request):
    return render(request, 'user_languages/index.html')

def login(request):
	if request.method == "POST":
		result = User.objects.login(
			email=request.POST['email'],
		 	password=request.POST['password']
		)
		print "~!@#"*50, result
		if result[0]:
			request.session['user_id'] = result[1].id
			return redirect(reverse('dashboard'))
		else:
			request.session['errors'] = result[1]
			return redirect(reverse('index'))

			print "no user found"
			return redirect(reverse('index'))


def register(request):
    if request.method == "POST":
        result = User.objects.register(
			first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=request.POST['password'], c_password=request.POST['c_password']
		)
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

# build out bcrypt (talk about), login, registration validation beforehand.
# then languages, ORM
# language.users.add(User)
#click on user's name, dropdown of languages for logged in user, make a language show page to show all users who like a particular language ( language.get(id=1).users() )
