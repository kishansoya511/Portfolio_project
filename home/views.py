from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("this is my homepage (/)")

def about(request):
    return HttpResponse("this is my about page (/about)")

def projects(request):
    return HttpResponse("this is my projects page (/project)")

def contact(request):
    return HttpResponse("this is my contact page (/contact)")