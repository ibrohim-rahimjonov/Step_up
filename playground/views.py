from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Request -> responce

def say_hello(request):
    return render(request,'hi.html',{'name':'Ibrohim'})
