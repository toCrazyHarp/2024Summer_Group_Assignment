from django.shortcuts import render
from django.http import HttpResponse

def Info(request):
    from Info.models import Tasks
    all_tasks = Tasks.objects.all()
    Index = range(1, all_tasks.count() + 1)
    Infomations = zip(all_tasks, Index)
    return render(request,"task_lists.html",{"Title":"所有日程安排","Info":Infomations})

def add(request):

    return render(request,"login.html")
def delete():
    return HttpResponse("this is delete page")
def edit(request):
    return HttpResponse("this is edit page")

