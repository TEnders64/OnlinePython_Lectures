from django.shortcuts import render, jsonify

# Create your views here.
def index(request):
	return HttpResponse('<h1>we made it</h1>')

def show(request, id):
	print id
	print type(id)
	return HttpResponse('<h1>This is the id:' + id  + '</h1>')

def whoa(request, **kwargs):
	print kwargs
	for key, arg in kwargs.items():
		print key, arg
	return jsonify(kwargs)
