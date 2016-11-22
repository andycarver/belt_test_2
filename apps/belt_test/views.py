from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    return render(request, 'belt_test/index.html')

    