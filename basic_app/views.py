from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'basic_app/index.html')

def user(request):
    return render(request,'basic_app/other.html')

def relatives(request):
    return render(request,'basic_app/relative_url_template.html')

# Create your views here.
