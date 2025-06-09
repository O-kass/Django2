from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")