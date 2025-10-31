from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jijarformat(request):
    return render(request,'jijar.html',{'name':'kerala','new':'hello world'},)


def add(request):
    n1=int(request.GET['num'])
    n2=int(request.GET['num2'])
    result=n1+n2

   
    return render(request,'result.html',{'s':result})


def newresult(request):
     n4=int(request.GET['firstnumber'])
     n5=int(request.GET['secondnumber'])
     n=n4+n5
     return render(request,'result.html',{'k':n})

