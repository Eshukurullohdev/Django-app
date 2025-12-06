from django.shortcuts import render
from django.http import HttpResponse
from .models import Tovar
# templates
# dict
# key
# value

# for 
def home(request):
    narsalar = Tovar.objects.all()
    return render(request, "home.html", {"narsalar": narsalar})


# click