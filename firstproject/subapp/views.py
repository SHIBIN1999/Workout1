from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jijarformat(request):
    return render(request,'jijar.html',{'name':'kerala'})


def add(request):
    n1=int(request.GET['num'])
    n2=int(request.GET['num2'])
    result=n1+n2
    return render(request,'result.html',{'s':result})