from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User, Language
# Create your views here.
def index(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'user_languages/index.html', context)
