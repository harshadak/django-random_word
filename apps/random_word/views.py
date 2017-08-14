from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
  
# the index function is called when root is visited
def index(request):
    # You don't need context object to store rand_word
    return render(request, "random_word/index.html")

def makeAWord(request):
    if request.method == "POST":
        request.session['rand_word'] = get_random_string(length=14)
        if "counter" in request.session:
            request.session['counter'] = request.session['counter'] + 1
        else:
            request.session['counter'] = 1
        return redirect("/")

def reset(request):
    try:
        del request.session['rand_word']
        del request.session['counter']
        return redirect("/")
    except:
        return redirect("/")