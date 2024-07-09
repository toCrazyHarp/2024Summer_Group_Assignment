from django.shortcuts import render
from django.http import HttpResponse
def mainpage(request):
    return HttpResponse("Hello, world. You're at the main page.")
# Create your views here.
