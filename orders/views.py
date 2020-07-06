from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Meal


# Create your views here.

def index(request):

	context = {
        'rp': Meal.objects.filter(category='RP'),
        'sp': Meal.objects.filter(category='SP'),
        'to': Meal.objects.filter(category='TO'),
        'su': Meal.objects.filter(category='SU'),
        'pa': Meal.objects.filter(category='PA'),
        'sa': Meal.objects.filter(category='SA'),
        'dp': Meal.objects.filter(category='DP')
    }

	return render(request, "index.html", context)


def login_view(request):

    return render(request, "login.html")

def login_request(request):

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})
