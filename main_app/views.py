from django.shortcuts import render
#Import HttpResponse to send text-base responses
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Django</h1>")