from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse('Hii')

def about (request):
    return HttpResponse("Aboutus")

def page (request):
    return render(request,'abc.html')