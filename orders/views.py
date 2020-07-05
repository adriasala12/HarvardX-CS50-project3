from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Pizza


# Create your views here.

def index(request):

	context = {
        "meals": Pizza.objects.all()
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
