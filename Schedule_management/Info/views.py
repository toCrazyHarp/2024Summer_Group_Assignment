from django.shortcuts import render
from django.http import HttpResponse

def Info(request):
    return render(request,"task_lists.html")
def add(request):
    return render(request,"login.html")
def delete():
    return HttpResponse("this is delete page")
def edit(request):
    return HttpResponse("this is edit page")

