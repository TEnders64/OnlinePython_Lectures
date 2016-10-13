from django.shortcuts import render
from .models import User, Book
# Create your views here.
def show_users(request):
    all_users = User.objects.all() # SELECT * FROM users
    print all_users
    print request
    return render(request, 'djangoApp/index.html')
#
# def show_books(request):
#     all_books = Book.objects.all()
