from django.http import HttpResponse
from django.shortcuts import render

# Simple views returning plain text
def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is the about page of MyApp. Learn more about us here.")

def contact(request):
        return render(request,'contact.html')
