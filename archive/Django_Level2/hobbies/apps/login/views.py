from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	users = User.objects.all()
	context = {
		'users': users
	}
	return render(request, 'login/index.html', context)

def register(request):
	if request.method == 'POST':
		response = User.objects.validate_registration(request.POST)
		if response[0]:
			request.session['first_name'] = response[1].first_name
			return redirect(success)
		else:
			for error in response[1]:
				messages.add_message(request, messages.WARNING, error)
	return redirect(index)

def success(request):
	return render(request, 'login/success.html')
