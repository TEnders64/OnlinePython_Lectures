from django.shortcuts import render, redirect, HttpResponse

from .models import Hobby

# Create your views here.
def index(request):
	if request.method == "POST":
		response_back = Hobby.objects.ValidateCreation(request.POST)
		print response_back

	date = Hobby.objects.get(id=3)
	date = date.created_at
	context = {
		'categories': ['sport', 'craft', 'outdoor', 'computer'],
		'hobby': Hobby.objects.get(id=1),
		'hobbies': Hobby.objects.all(),
		'datetime': date
	}
	hobbies = Hobby.objects.get(id=2)
	print context['hobby']

	return render(request, 'hobby_app/index.html', context)
