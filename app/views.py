from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return HttpResponseRedirect('home')


def home(request):
    context = {}
    return render(request, 'app/home.html', context)


def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)


def results(request):
    context = {}
    return render(request, 'app/results.html', context)

