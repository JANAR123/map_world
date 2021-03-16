from django.shortcuts import render
from .forms import LocationForm
from django.http import HttpResponse


# Create your views here.

def maps(request):
    
    form=LocationForm()
    if request.method=="POST":
        print(request.POST)
        return  HttpResponse
    return render(request,'maps.html',{'form':form})