#from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    #return HttpResponse("Hello World!,I am Home.")
    return render(request,'home.html')

def aboutPage(request):
    #return HttpResponse("I am about page.")
    return render(request,'about.html')