from django.shortcuts import render
#Import HttpResponse to send text-base responses
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Django</h1>")
def about(request):
    return render(request, 'about.html')

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats =[
    Cat('Lolo', 'tabby', 'kinda rude', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle', 0),
    Cat('Fancy', 'bombay', 'Happy fluffball', 3),
]

def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})
