from django.shortcuts import render
from App.models import User_villalist ,User_weivilla,User_tuijian
from django.core.paginator import Paginator
# Create your views here.
def properties(request,page=1):
    # 大别墅
    dbs = User_weivilla.objects.all()
    # 别墅样式
    dby = User_villalist.objects.all()
    # 一页8个
    paginator = Paginator(dbs,9)
    # 创建分页对象
    page = int(page)
    pagination = paginator.page(page)

    if paginator.num_pages > 10:
        if page - 5 <= 0:
            customRange = range(1, 11)
        elif page + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(page - 5, page + 4)
    else:
         customRange = paginator.page_range
    #推荐参数
    #所有推荐别墅
    dbb = User_tuijian.objects.all()
    username = request.session.get("username")
    return render(request, 'properties.html',context={
        "dbss":pagination.object_list,
        "dbys":dby,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'dbb': dbb,
        'username': username,
        'session': request.session
    })





def properties2(request,page=1):
    # 大别墅
    dbs = User_weivilla.objects.all()
    # 别墅样式
    dby = User_villalist.objects.all()
    # 一页8个
    paginator = Paginator(dbs, 9)
    # 创建分页对象
    page = int(page)
    pagination = paginator.page(page)

    if paginator.num_pages > 10:
        if page - 5 <= 0:
            customRange = range(1, 11)
        elif page + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(page - 5, page + 4)
    else:
        customRange = paginator.page_range

    # 推荐参数
    # 所有推荐别墅
    dbb = User_tuijian.objects.all()
    username = request.session.get("username")
    return render(request, 'properties2.html', context={
        "dbss": pagination.object_list,
        "dbys": dby,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'dbb': dbb,
        'username': username,
        'session': request.session
    })






def properties3(request,page=1):
    # 大别墅
    dbs = User_weivilla.objects.all()
    # 别墅样式
    dby = User_villalist.objects.all()

    #分页
    # 一页8个
    paginator = Paginator(dbs,9)
    # 创建分页对象
    page = int(page)
    pagination = paginator.page(page)
        #如何总页数大于5进行自定义页码范围，如果不大于5 直接显示5页
    if paginator.num_pages > 10:
        #如何当前页页码减小于0，从1显示到5页
        if page - 5 <= 0:
            customRange = range(1, 11)
        elif page + 4 > paginator.num_pages:
             #如何当前页+5页大了总页数
             customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
             customRange = range(page - 5, page + 5)
    else:#页码总数小于5
         customRange = paginator.page_range


    #推荐参数
    #所有推荐别墅
    dbb = User_tuijian.objects.all()
    username = request.session.get("username")
    return render(request, 'properties3.html',context={
        "dbss":pagination.object_list,
        "dbys":dby,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'dbb': dbb,
        'username': username,
        'session': request.session
    })