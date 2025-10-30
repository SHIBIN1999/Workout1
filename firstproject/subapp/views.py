from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jijarformat(request):
    return render(request,'jijar.html',{'name':'kerala'})