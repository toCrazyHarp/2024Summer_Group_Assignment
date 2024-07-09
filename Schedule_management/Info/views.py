from django.shortcuts import render
from django.http import HttpResponse

def Info(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
