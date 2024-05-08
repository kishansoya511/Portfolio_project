from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("this is my home page (/)")
    context = {'name':'harry','course':'Django'}
    return render(request,'home.html',context)


def about(request):
    # return HttpResponse("this is my about page (/about)")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("this is my projects page (/project)")
    return render(request,'projects.html')

def contact(request):
    # return HttpResponse("this is my contact page (/contact)")
    return render(request,'contact.html')