from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def Info(request):
    return render(request, "hello")


def shorter(request):
    from Info.models import Tasks
    from datetime import datetime
    from django.urls import reverse
    from django.shortcuts import redirect
    all_tasks = Tasks.objects.all()
    Index = range(1, all_tasks.count() + 1)
    Infomations = zip(all_tasks, Index)
    if request.method == 'POST':
        title = request.POST.get('title')
        start_time = datetime.now()  # 获取当前时间
        is_checked = 0  # 默认设置为0
        Tasks.objects.create(title=title, start_time=start_time, ischecked=is_checked)
        return redirect(reverse(shorter))  # 重定向到成功页面或任何你想要的页面
    return render(request, "task_lists.html", {"Title": "所有日程安排", "Info": Infomations})


def longer(request):
    from Info.models import longperiodtasks
    from datetime import datetime
    from django.urls import reverse
    from django.shortcuts import redirect
    all_tasks = longperiodtasks.objects.all()
    Index = range(1, all_tasks.count() + 1)
    Infomations = zip(all_tasks, Index)
    if request.method == 'POST':
        title = request.POST.get('title')
        end_date = request.POST.get('end_date')
        start_time = datetime.now()  # 获取当前时间
        is_checked = 0  # 默认设置为0
        longperiodtasks.objects.create(title=title, start_time=start_time, end_time = end_date,ischecked=is_checked)
        return redirect(reverse(longer))
    return render(request, "task_lists1.html", {"Title": "所有日程安排", "Info": Infomations})


def routine(request):
    from Info.models import routinetasks
    from datetime import datetime
    from django.urls import reverse
    from django.shortcuts import redirect
    all_tasks = routinetasks.objects.all()
    Index = range(1, all_tasks.count() + 1)
    Infomations = zip(all_tasks, Index)
    if request.method == 'POST':
        title = request.POST.get('title')
        mode = request.POST.get('mode')
        start_time = datetime.now()  # 获取当前时间
        is_checked = 0  # 默认设置为0
        routinetasks.objects.create(title=title, mode=mode)
        return redirect(reverse(routine))
    return render(request, "task_lists2.html", {"Title": "所有日程安排", "Info": Infomations})


def add(request):
    return render(request, "window1.html")


def mainpage(request):
    from Info.models import famoussentencestasks
    from django.db.models import Count
    from Info.models import Tasks

    import random
    max_count = 6
    # 获取所有ischecked为False的记录ID，并转换为列表
    unchecked_ids = list(Tasks.objects.filter(ischecked=False).values_list('id', flat=True))
    # 如果没有满足条件的记录，可以选择返回一个空的QuerySet或其他适当的响应
    if not unchecked_ids:
        # 返回一个空的QuerySet，这样调用者可以像处理其他QuerySet一样处理它
        return Tasks.objects.none()

        # 如果记录数少于或等于max_count，则不需要随机选择
    if len(unchecked_ids) <= max_count:
        random_ids = unchecked_ids
    else:
        # 否则，从unchecked_ids中随机选择max_count个ID
        random_ids = random.sample(unchecked_ids, max_count)

        # 使用这些ID来获取并返回Tasks记录
    random_tasks = Tasks.objects.filter(id__in=random_ids)
    uncheckedtasks = Tasks.objects.filter(ischecked=False)
    all_tasks = famoussentencestasks.objects.order_by('?').first()

    return render(request, "mainpage.html",
                  {"sentences": all_tasks, 'randomtasks': random_tasks, 'tasks': uncheckedtasks})


def get_data(request):
    from Info.models import Tasks
    from django.db.models import Count
    from django.db.models.functions import TruncDate
    import json
    data = Tasks.objects.annotate(
        date=TruncDate('start_time')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')
    echarts_data = []
    for item in data:
        echarts_data.append([
            item['date'].strftime('%Y-%m-%d'),  # 格式化日期
            item['count']  # 计数
        ])
    return JsonResponse(echarts_data, safe=False)


def search_results(request):
    from Info.models import Tasks
    query = request.GET.get('query', '')
    if query:
        # 使用__icontains进行不区分大小写的模糊搜索
        results = Tasks.objects.filter(title=query)
    else:
        # 如果没有查询词，可以选择返回一个空查询集或者所有记录
        results = Tasks.objects.none()  # 返回一个空的查询集
        # 或者返回所有记录：results = MyModel.objects.all()
    context = {'query': query, 'results': results}
    return render(request, 'search_results.html', context)


def add_task(request):
    from Info.models import Tasks
    from datetime import datetime
    from django.urls import reverse
    from django.shortcuts import redirect

    if request.method == 'POST':
        title = request.POST.get('title')
        start_time = datetime.now()  # 获取当前时间
        is_checked = 0  # 默认设置为0
        Tasks.objects.create(title=title, start_time=start_time, ischecked=is_checked)
        return redirect(reverse('main'))  # 重定向到成功页面或任何你想要的页面
    return redirect(reverse('main'))  # 如果不是POST请求，渲染相同的页面或另一个页面
