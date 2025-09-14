from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('RANIEL DOMINGO STUDENT ID:2023-25016')

def home(request):
    return render(request, "home.html", {"title": "Home"})
