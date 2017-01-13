from django.shortcuts import render
import random
import string
alphanum = []
for letter in string.ascii_lowercase:
    alphanum.append(letter)
for num in range(0,10):
    alphanum.append(num)
# Create your views here.

def index(request):
    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 1

    word = ""
    for num in range(0,14):
        word += str(random.choice(alphanum))

    context = {
        'word': word
    }
    return render(request, 'randWord/index.html', context)
