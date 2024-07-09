from django.shortcuts import render
from django.http import HttpResponse

def Info(request):
    return render(request,"task_lists.html")
def add(request):
    return HttpResponse("this is add page")
def delete():
    return HttpResponse("this is delete page")
def edit(request):
    return HttpResponse("this is edit page")

