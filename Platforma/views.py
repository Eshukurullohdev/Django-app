from django.shortcuts import render
from django.http import HttpResponse
from  .models import Tovar, Items
# templates
# dict
# key
# value
# for 
def home(request):
    narsalar = Tovar.objects.all()
    return render(request, "home.html", {"narsalar": narsalar})

def second_html(request):
    ikkinchi = Items.objects.all()
    return render(request, "second_html.html", {"ikkinchi": ikkinchi})


def base(request):
    return render(request, "base.html")

def navigation(request):
    return render(request, "navigation.html")
# click