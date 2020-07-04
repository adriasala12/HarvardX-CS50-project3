from django.http import HttpResponse
from django.shortcuts import render
from .models import Meal

# Create your views here.
def index(request):

    context = {
        "meals": Meal.objects.all()
    }

    return render(request, "index.html", context)
